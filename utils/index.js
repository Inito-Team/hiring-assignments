const { readFileSync, writeFileSync } = require('node:fs');
const chalk = require('chalk')

const log = console.log;

let fileSystem = {};
let savedData = null;
let inMemoryPath = null;

let currDirObjRef = {};
let currDir = [];

function setCurrDirObjRef(ref) {
    currDirObjRef = ref;
}

function setCurrDir(dir) {
    currDir = dir;
}

function loadState(path) {
    if(path) {
        try {
            savedData = readFileSync(path);
        } catch (e) { }
    }
}

function setFileSystem(path) {
    inMemoryPath = path;
    if (inMemoryPath && savedData && savedData.buffer.byteLength > 1)
        fileSystem = JSON.parse(savedData) || {};//this is the actual file system;

    if (!fileSystem.hasOwnProperty('/'))
        fileSystem['/'] = {}; //actual file system where everything will be stored

    currDir = ['/']; //will be used to keep track of the current working directory path
    currDirObjRef = fileSystem['/']; //always holds the current directory reference
}

function saveCurrentDirState() {
    if(inMemoryPath) 
        writeFileSync(inMemoryPath, JSON.stringify(fileSystem));
}

function getDirData(dirObj, name) { // whole directory, and the path from which you are starting;
    if (typeof dirObj !== 'object')
        return null;
    if (typeof (dirObj) === 'object' && dirObj.hasOwnProperty(name))
        return dirObj[name];

    for (let file of Object.keys(dirObj)) {
        const foundData = getDirData(dirObj[file], name);
        if (foundData)
            return foundData;
    }
    return null;
}

function getDirectoryObjRef(path = "") { //to get the directory ref object;
    if (path === '/' || path === '~') {
        return [['/'], fileSystem['/']];
    }
    const dirPaths = path.split('/').map(item => item.trim());
    const tempDir = [...currDir];
    // console.log(oldDir)

    for (let currPath of dirPaths) {
        // console.log(currPath)
        if (!currPath || currPath === '.' || currPath === '/')
            continue;
        if (currPath === '..')
            if (tempDir.length > 1)
                tempDir.pop();
            else
                continue;
        else
            tempDir.push(currPath);
    }
    const lastDir = tempDir[tempDir.length - 1];

    let isPathCorrect = true;
    let tempFileSystem = { ...fileSystem };

    for (let dir of tempDir) { //handle no valid path
        if (tempFileSystem.hasOwnProperty(dir)) {
            tempFileSystem = tempFileSystem[dir];
        } else {
            isPathCorrect = false;
            break;
        }
    }

    if (!isPathCorrect) { //if it is a wrong path
        return null;
    }

    //valid path
    return [tempDir, listCurrentDirectory(lastDir)];
    // console.log(currDir)
}

function listCurrentDirectory(dir = currDir) { // to see the content of the current working directory act like a `ls`
    return getDirData(fileSystem, dir);
}

function createDirectory(dirName) { // to create a directory in a pwd act like a `mkdir`
    currDirObjRef[dirName] = {};
}

function createFile(fileName, fileContent = '', fileDirObjRef = currDirObjRef) { // to create a new file in pwd 
    fileDirObjRef[fileName] = fileContent
}


function listDirectory(path) { //ls
    const dirRef = getDirectoryObjRef(path);
    if (!dirRef) {
        log(chalk.red.bold("Not a valid Directory Path"));
        return;
    }

    let logOutput = "";
    const fileDirectoryRef = dirRef[1] || currDirObjRef;
    for (let file of Object.keys(fileDirectoryRef)) {
        if (typeof fileDirectoryRef[file] === 'object')
            logOutput += chalk.blue.bold(file) + ' ';
        else
            logOutput += chalk.white(file) + ' ';
    }
    console.log(logOutput)
}

function pwd() { //pwd
    return currDir.length > 1 ? chalk.blue.bold(currDir.slice(1).join('/')) : '';
}

function readFile(filePath) { //cat
    const fileArray = filePath.split('/');

    const fileName = fileArray.pop();
    const dirRef = getDirectoryObjRef(fileArray.join('/'));
    if (!dirRef) {
        log(chalk.red.bold("Not a valid Directory Path"));
        return;
    }
    const fileDirectoryRef = dirRef[1];
    if (typeof fileDirectoryRef[fileName] !== 'object')
        return fileDirectoryRef[fileName];

    // if(typeof currDirObjRef[name]!=='object' && currDirObjRef.hasOwnProperty(name))
    //     return currDirObjRef[name];
    return chalk.red('No file Found');
}

function copyFile(srcPath = "", destPath = "") { //cp
    const srcArray = srcPath.split('/');
    const destArray = destPath.split('/');

    const srcFileName = srcArray.pop();
    const destinationFileName = srcFileName

    //remaining is the path;
    const srcDirRef = getDirectoryObjRef(srcArray.join('/'));
    const destDirRef = getDirectoryObjRef(destArray.join('/'))
    if (!srcDirRef || !destDirRef) {
        log(chalk.red.bold("Not a valid Directory Path"));
        return;
    }
    const srcFileDirectoryRef = srcDirRef[1];
    const destinationFileDirectoryRef = destDirRef[1];

    destinationFileDirectoryRef[destinationFileName] = srcFileDirectoryRef[srcFileName];
    return { destinationFileDirectoryRef, srcFileDirectoryRef, srcFileName, destinationFileName }
}

function moveFile(srcPath = "", destPath = "") { //mv;
    const { srcFileDirectoryRef, srcFileName } = copyFile(srcPath, destPath);
    delete srcFileDirectoryRef[srcFileName];
}

function removeFile(filePath) { //rm the file or directory
    const fileArray = filePath.split('/');

    const fileName = fileArray.pop();

    const dirRef = getDirectoryObjRef(fileArray.join('/'));
    if (!dirRef) {
        log(chalk.red.bold("Not a valid Directory Path"));
        return;
    }
    const fileDirectoryRef = dirRef[1];

    delete fileDirectoryRef[fileName];
};

function find(dirObj, regex, output = []) {
    for (let file of Object.keys(dirObj)) {
        if (typeof dirObj[file] !== 'object') {
            const fileContent = dirObj[file];
            const reg = new RegExp(regex);

            if (reg.test(fileContent))
                output.push(file);
        }
        else
            find(dirObj[file], regex, output);
    }
    return output;
}

function grep(regex, fileData = "") {
    regex = new RegExp(regex, 'g')
    const allMatches = fileData.match(regex);
    if (allMatches) return allMatches.length;
    return 0;
}

module.exports = {
    loadState,
    setFileSystem,
    listDirectory,
    getDirectoryObjRef,
    readFile,
    createDirectory,
    pwd,
    createFile,
    copyFile,
    moveFile,
    removeFile,
    grep,
    find,
    saveCurrentDirState,
    setCurrDir,
    setCurrDirObjRef
}