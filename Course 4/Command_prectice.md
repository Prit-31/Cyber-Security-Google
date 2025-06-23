# 🐧 Basic Linux Shell Commands

A beginner-friendly list of essential Linux shell commands for daily use.

---

## 📁 File & Directory Navigation

| Command | Description |
|---------|-------------|
| `pwd` | Show current directory path |
| `ls` | List files in current directory |
| `ls -l` | Long listing with details |
| `ls -a` | List all files including hidden |
| `cd [directory]` | Change directory |
| `cd ..` | Move one level up |
| `cd ~` | Go to home directory |

---

## 📄 File Operations

| Command | Description |
|---------|-------------|
| `touch file.txt` | Create an empty file |
| `cat file.txt` | View file content |
| `cp source.txt destination.txt` | Copy a file |
| `mv oldname.txt newname.txt` | Rename or move a file |
| `rm file.txt` | Delete a file |
| `nano file.txt` | Open file in nano editor |
| `vim file.txt` | Open file in vim editor |
| `echo "Hello" > file.txt` | Write to file (overwrite) |
| `echo "World" >> file.txt` | Append to file |

---

## 📂 Directory Operations

| Command | Description |
|---------|-------------|
| `mkdir new_folder` | Create a new directory |
| `rmdir folder` | Remove an empty directory |
| `rm -r folder` | Remove directory with contents |
| `tree` | Show directory structure (if installed) |

---

## 🔍 Searching

| Command | Description |
|---------|-------------|
| `find . -name "file.txt"` | Find file in current dir and subdirs |
| `grep "text" file.txt` | Search for text in a file |

---

## 📦 Package Management (Debian/Ubuntu)

| Command | Description |
|---------|-------------|
| `sudo apt update` | Update package list |
| `sudo apt upgrade` | Upgrade all packages |
| `sudo apt install [package]` | Install a package |
| `sudo apt remove [package]` | Uninstall a package |

---

## 🔐 Permissions

| Command | Description |
|---------|-------------|
| `chmod +x file.sh` | Make a script executable |
| `ls -l` | Check file permissions |
| `chown user:group file.txt` | Change ownership |

---

## ⚙️ System Info & Utilities

| Command | Description |
|---------|-------------|
| `whoami` | Show current user |
| `uname -a` | Show system info |
| `top` or `htop` | Show running processes |
| `df -h` | Disk space usage |
| `free -h` | Memory usage |
| `history` | Show command history |
| `clear` | Clear the terminal |

---

## 💡 Tips

- Use `TAB` for autocompletion.
- Use `Ctrl + C` to stop running command.
- Use `Ctrl + L` to clear screen (like `clear`).
- Use `man [command]` for help on any command (e.g., `man ls`).

---

**Save this file as** `linux_basics.md`  
Use `cat linux_basics.md` or open it in any Markdown viewer.

