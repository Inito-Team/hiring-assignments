// filesystem.h
#pragma once
#include <string.h>
#include <bits/stdc++.h>
using namespace std;

class InMemoryFileSystem
{
public:
    InMemoryFileSystem();
    void mkdirRec(string &dir, unordered_map<string, unordered_map<string, string>> fs);
    void mkdir(string &directoryName, InMemoryFileSystem &fs);
    void cd(string &path);
    void ls(string &path, InMemoryFileSystem &fs);
    void touch(string &fileName);
    void cat(string &fileName);
    void echo(string &text, string &fileName);
    void mv(string &source, string &destination);
    void cp(string &source, string &destination);
    void rm(string &path);
    void printFileSystem();

    void grep(string &pattern, string fileName);

private:
    string currentDirectory;
    unordered_map<string, unordered_map<string, string>> fileSystem;

    string getAbsolutePath(string &path);
};
