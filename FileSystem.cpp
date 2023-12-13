#include "FileSystem.h"
#include <iostream>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <bits/stdc++.h>

namespace FileSystemNamespace
{
    FileSystem::FileSystem()
    {
        root = new Node();
        currentDir = root;
    }

    FileSystem::~FileSystem()
    {
        destroy(root);
    }

    void FileSystem::mkdir(const std::string &directory)
    {
        if (currentDir->children.find(directory) == currentDir->children.end())
        {
            currentDir->children[directory] = new Node();
            std::cout << "Directory '" << directory << "' created." << std::endl;
        }
        else
        {
            std::cout << "Directory '" << directory << "' already exists." << std::endl;
        }
    }

    void FileSystem::cd(const std::string &directory)
    {
        if (directory == "/")
        {
            currentDir = root;
        }
        else if (directory == "..")
        {
            if (currentDir != root)
            {
                currentDir = getParent(currentDir);
            }
        }
        else if (directory[0] == '/')
        {
            Node *targetDir = findPath(root, parsePath(directory));
            if (targetDir)
            {
                currentDir = targetDir;
            }
            else
            {
                std::cout << "Directory '" << directory << "' not found." << std::endl;
            }
        }
        else
        {
            Node *targetDir = currentDir->children[directory];
            if (targetDir && !targetDir->isFile)
            {
                currentDir = targetDir;
            }
            else
            {
                std::cout << "Directory '" << directory << "' not found." << std::endl;
            }
        }
    }

    void FileSystem::ls() const
    {
        std::cout << "Contents of '" << getCurrentPath() << "':" << std::endl;
        for (const auto &entry : currentDir->children)
        {
            std::cout << "  " << entry.first << (entry.second->isFile ? " (file)" : " (directory)") << std::endl;
        }
    }

    void FileSystem::touch(const std::string &filename)
    {
        if (currentDir->children.find(filename) == currentDir->children.end())
        {
            currentDir->children[filename] = new Node(true);
            std::cout << "File '" << filename << "' created." << std::endl;
        }
        else
        {
            std::cout << "File '" << filename << "' already exists." << std::endl;
        }
    }

  void FileSystem::echo(const std::string &text, const std::string &filename) {
    // Remove quotes from the filename if present
    std::string cleanedFilename = filename;
    if (!cleanedFilename.empty() && cleanedFilename.front() == '"' && cleanedFilename.back() == '"') {
        cleanedFilename = cleanedFilename.substr(1, cleanedFilename.size() - 2);
    }

    Node *file = currentDir->children[cleanedFilename];
    if (file && file->isFile) {
        file->content = text;
        std::cout << "Text written to '" << cleanedFilename << "'." << std::endl;
    } else {
        std::cout << "File '" << cleanedFilename << "' not found." << std::endl;
    }
}


    void FileSystem::cat(const std::string &filename) const
    {
        Node *file = currentDir->children[filename];
        if (file && file->isFile)
        {
            std::cout << file->content << std::endl;
        }
        else
        {
            std::cout << "File '" << filename << "' not found." << std::endl;
        }
    }

    void FileSystem::mv(const std::string &source, const std::string &destination)
    {
        Node *sourceNode = currentDir->children[source];
        Node *destinationNode = currentDir->children[destination];

        if (sourceNode)
        {
            if (!destinationNode)
            {
                currentDir->children[destination] = sourceNode;
                currentDir->children.erase(source);
                std::cout << "Moved '" << source << "' to '" << destination << "'." << std::endl;
            }
            else
            {
                std::cout << "Destination '" << destination << "' already exists." << std::endl;
            }
        }
        else
        {
            std::cout << "Source '" << source << "' not found." << std::endl;
        }
    }

    void FileSystem::cp(const std::string &source, const std::string &destination)
    {
        Node *sourceNode = currentDir->children[source];
        Node *destinationNode = currentDir->children[destination];

        if (sourceNode)
        {
            if (!destinationNode)
            {
                currentDir->children[destination] = new Node(sourceNode->isFile, sourceNode->content);
                std::cout << "Copied '" << source << "' to '" << destination << "'." << std::endl;
            }
            else
            {
                std::cout << "Destination " << destination << "' already exists." << std::endl;
            }
        }
        else
        {
            std::cout << "Source '" << source << "' not found." << std::endl;
        }
    }

    void FileSystem::rm(const std::string &item)
    {
        Node *itemNode = currentDir->children[item];

        if (itemNode)
        {
            destroy(itemNode);
            currentDir->children.erase(item);
            std::cout << "Removed '" << item << "'." << std::endl;
        }
        else
        {
            std::cout << "Item '" << item << "' not found." << std::endl;
        }
    }

    FileSystem::Node *FileSystem::getParent(Node *node) const
    {
        for (auto &entry : root->children)
        {
            if (entry.second == node)
            {
                return root;
            }
            Node *parent = getParent(entry.second);
            if (parent)
            {
                return parent;
            }
        }
        return nullptr;
    }

    FileSystem::Node *FileSystem::findPath(Node *node, const std::vector<std::string> &path) const
    {
        if (path.empty())
        {
            return node;
        }

        const std::string &nextDir = path.front();
        auto it = node->children.find(nextDir);
        if (it != node->children.end())
        {
            return findPath(it->second, std::vector<std::string>(path.begin() + 1, path.end()));
        }

        return nullptr;
    }

    std::vector<std::string> FileSystem::parsePath(const std::string &path) const
    {
        std::vector<std::string> result;
        std::istringstream iss(path);
        std::string token;

        while (getline(iss, token, '/'))
        {
            if (!token.empty())
            {
                result.push_back(token);
            }
        }

        return result;
    }

    std::string FileSystem::getCurrentPath() const
    {
        std::vector<std::string> path;
        Node *current = currentDir;

        while (current != root)
        {
            for (auto &entry : getParent(current)->children)
            {
                if (entry.second == current)
                {
                    path.push_back(entry.first);
                    current = getParent(current);
                    break;
                }
            }
        }

        reverse(path.begin(), path.end());

        return '/' + (path.empty() ? "" : (accumulate(path.begin(), path.end(), std::string("/"))));
    }

    void FileSystem::destroy(Node *node)
    {
        for (auto &entry : node->children)
        {
            destroy(entry.second);
        }
        delete node;
    }
}