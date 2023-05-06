# MacOS CheatSheet

## (Homebrew Basics)[brew]
## To list all JDK 
```shell
/usr/libexec/java_home -V
Matching Java Virtual Machines (7):
    20.0.1 (x86_64) "Amazon.com Inc." - "Amazon Corretto 20" /Users/tanmaysaha/Library/Java/JavaVirtualMachines/corretto-20.0.1/Contents/Home
    19.0.2 (x86_64) "Amazon.com Inc." - "Amazon Corretto 19" /Users/tanmaysaha/Library/Java/JavaVirtualMachines/corretto-19.0.2/Contents/Home
    17.0.4 (x86_64) "Amazon.com Inc." - "Amazon Corretto 17" /Users/tanmaysaha/Library/Java/JavaVirtualMachines/corretto-17.0.4.1/Contents/Home
    11.0.8 (x86_64) "AdoptOpenJDK" - "AdoptOpenJDK 11" /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home
    1.8.261.12 (x86_64) "Oracle Corporation" - "Java" /Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home
    1.8.0_161 (x86_64) "Oracle Corporation" - "Java SE 8" /Library/Java/JavaVirtualMachines/jdk1.8.0_161.jdk/Contents/Home
    1.8.0_111 (x86_64) "Oracle Corporation" - "Java SE 8" /Library/Java/JavaVirtualMachines/jdk1.8.0_111.jdk/Contents/Home
```

## jEnv - Manage your Java environment
1. [jenv](https://www.jenv.be)
2. [Managing Multiple JDK Installations With jEnv](https://www.baeldung.com/jenv-multiple-jdk)

There are a couple of things more that you need to do to get it working properly…

Run the following commands if you are using maven :

```shell
  $ jenv enable-plugin maven
  $ jenv enable-plugin export
```

PS : If you get errors stating that the command enable-plugin is not found, you must restart your terminal and things should work properly thereafter.

I had to run jenv enable-plugin export because my jenv was not able to control my JAVA_HOME. Also failing to run jenv enable-plugin maven will throw weird errors when trying to compile your project.

Now.. You are all set…

Verify
You mostly only will need to use jenv local to set the java version for your project. You may cd to your project directory and type
```shell
  $ jenv local 10.0
```  
With this command, a   .**java-version** file gets auto created in your project directory. You may opt to add this file in .**gitignore** list (if you want).

Now, if you type
```sell
  $ echo $JAVA_HOME
  OR
  $ javac -version
```  
  
