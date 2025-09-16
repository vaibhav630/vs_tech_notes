# Install & Run Java JDK on Mac

---
## 1. Download & Install JDK

* Go to: [Oracle Java Downloads](https://www.oracle.com/java/technologies/downloads/)
* Select **macOS → DMG Installer**:

  * **ARM64** → for M1/M2 Macs
  * **x64** → for Intel Macs
* Open `.dmg` → run `.pkg` → complete installation.

---

## 2. Set JAVA\_HOME

Open Terminal:
run this command and note down the version
```bash
/usr/libexec/java_home -V
```

Edit `~/.zshrc`:
```bash
nano ~/.zshrc
```
If .zshrc is not available in home directory, then create new file:
```bash
touch .zshrc
```

Add lines (replace version with yours):
```bash
export JAVA_HOME=$(/usr/libexec/java_home -v <version>)
export PATH=$JAVA_HOME/bin:$PATH
```

Save & reload:

```bash
source ~/.zshrc
```

Check:

```bash
echo $JAVA_HOME
java -version
```

---

## 3. Compile & Run Java Program

```bash
cd ~/Documents
mkdir my-project && cd my-project
touch Hello.java
```

Add content to `Hello.java`:

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

Compile & run:

```bash
javac Hello.java
java Hello
```

---

✅ Java installed, `JAVA_HOME` set, and program running successfully.

---