#include <iostream>
#include <bits/stdc++.h>

#include "FileSystem.h"

using namespace std;


int main()
{
    FileSystemNamespace::FileSystem fileSystem;

    while (true)
    {
        cout << "> Enter command: ";
        string command;
        getline(cin, command);

        if (command == "exit")
        {
            break;
        }

       istringstream iss(command);
string token;
vector<string> tokens;

while (iss >> token) {
    tokens.push_back(token);
}

if (tokens.empty()) {
    continue;
}

string action = tokens[0];
vector<string> args(tokens.begin() + 1, tokens.end());

        if (action == "mkdir")
        {
            if (!args.empty())
            {
                fileSystem.mkdir(args[0]);
            }
            else
            {
                cout << "Usage: mkdir <directory>" << endl;
            }
        }
        else if (action == "cd")
        {
            if (!args.empty())
            {
                fileSystem.cd(args[0]);
            }
            else
            {
                cout << "Usage: cd <directory>" << endl;
            }
        }
        else if (action == "ls")
        {
            fileSystem.ls();
        }
        else if (action == "touch")
        {
            if (!args.empty())
            {
                fileSystem.touch(args[0]);
            }
            else
            {
                cout << "Usage: touch <filename>" << endl;
            }
        }
        else if (action == "echo")
        {
            if (!args.empty())
            {
                fileSystem.echo(args[0], args[1]);
            }
            else
            {
                cout << "Usage: echo <text> <filename>" << endl;
            }
        }
        else if (action == "cat")
        {
            if (!args.empty())
            {
                fileSystem.cat(args[0]);
            }
            else
            {
                cout << "Usage: cat <filename>" << endl;
            }
        }
        else if (action == "mv")
        {
            if (args.size() == 2)
            {
                fileSystem.mv(args[0], args[1]);
            }
            else
            {
                cout << "Usage: mv <source> <destination>" << endl;
            }
        }
        else if (action == "cp")
        {
            if (args.size() == 2)
            {
                fileSystem.cp(args[0], args[1]);
            }
            else
            {
                cout << "Usage: cp <source> <destination>" << endl;
            }
        }
        else if (action == "rm")
        {
            if (!args.empty())
            {
                fileSystem.rm(args[0]);
            }
            else
            {
                cout << "Usage: rm <item>" << endl;
            }
        }
        else
        {
            cout << "Invalid command. Supported commands: mkdir, cd, ls, touch, echo, cat, mv, cp, rm, exit" << endl;
        }
    }

    return 0;
}