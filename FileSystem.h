#ifndef FILESYSTEM_H
#define FILESYSTEM_H

#include <iostream>
#include <unordered_map>
#include <vector>

namespace FileSystemNamespace
{

    class FileSystem
    {
    private:
        struct Node
        {
            bool isFile;
            std::string content;
            std::unordered_map<std::string, Node *> children;

            Node(bool isFile = false, const std::string &content = "") : isFile(isFile), content(content) {}
        };

        Node *root;
        Node *currentDir;

    public:
        FileSystem();
        ~FileSystem();

        void mkdir(const std::string &directory);
        void cd(const std::string &directory);
        void ls() const;
        void touch(const std::string &filename);
        void echo(const std::string &text, const std::string &filename);
        void cat(const std::string &filename) const;
        void mv(const std::string &source, const std::string &destination);
        void cp(const std::string &source, const std::string &destination);
        void rm(const std::string &item);

    private:
        Node *getParent(Node *node) const;
        Node *findPath(Node *node, const std::vector<std::string> &path) const;
        std::vector<std::string> parsePath(const std::string &path) const;
        std::string getCurrentPath() const;
        void destroy(Node *node);
    };

} // namespace FileSystemNamespace

#endif
