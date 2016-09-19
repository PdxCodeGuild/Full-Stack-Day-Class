# CLI Shell Fu

You've learned [the basics](/notes/cli.md) of navigating and using the CLI, but you can really streamline many many common operations and text editing.

## Editing Shortcuts

* `C-` means press **control**
* `M-` means press **alt**

In general, control operates on one _character_, meta operates on one _word_.

### Cursor Movement

No need to move your hands to the arrow keys!

* `C-e` end of command
* `C-a` beginning of command (A for beginning of alphabet)

* `C-f` forward character
* `C-b` backward character
* `M-f` forward word
* `M-b` backward word

### Deletion

* `D-d` delete forwards character
* `M-backspace` delete backward word
* `M-d` delete forwards word

* `C-k` delete to end of command
* `C-u` delete to beginning of command

### Modification

* `M-u` uppercase next word
* `M-l` lowercase next word
* `M-c` capitalize next word

* `C-t` transpose characters
* `M-t` transpose words

## History

* `C-n` next command, like `down`
* `C-p` previous command, like `up`

* `C-r` search history (R for reverse search); can edit before running

You can refer to parts of the previous command using **history expansions**.
They are like "variables" that start with exclamation point `!`.

* `!!$` just the last word of the previous command (`$` was the "end of string" regexp token)
* `!!0` just the first word of the previous command

To go back to the previous directory `cd -`.

## Aliases

For common complex, you can make named shortcuts called **aliases**.

```bash
alias gl="git log"
```

If a command you write starts with an alias, it is expanded.
Other stuff can come after too.

```bash
gl --oneline
```

Folks also use aliases as a way to sort of set "defaults" on a command.
Aliases are resolved before commands, so this works.

```bash
alias rm='rm -iv'
```

If you ever want an alias to explicitly not be resolved, escape the command with a backslash `\`.

```bash
\rm FILES...
```

If you save these alias making commands in your `.bashrc` file, you can have them on every shell startup.

## IO Redirection

To take standard out of one command and make it the input of another command, use pipe `|`.
This is called **IO redirection** or **piping**.
You can chain together as many of these as you want.

```bash
ls | egrep hi | wc -l
```

To write output to a file, use greater-than `>`.

```bash
git log > all_history.txt
```

To "split" a text pipeline, you can use `tee`.
It writes its input to a file and also passes it through.

```bash
ls | tee files.txt | wc -l
```

You can also take the output of a command and turn it into command line arguments using **command substitution** with dollar sign parentheses `$()`.

```bash
mv $(find . -name '*.py') vault
```

These, by default, only redirect **standard out**.
Many commands also write to **standard error**, which is another path for program output.

## Globbing

You can get the shell to expand the run command to include files under the current directory that match a pattern.
That process is called **globbing**.
Remember, the command is expanded to include matching files _before it even runs_.
Like mini regular expressions.

* `*` is any number of characters in that slot
* `?` is any single character
* `**/` is every directory under the current recursively
* `{A,B}` is a list of choices; will product all of them

Say you have a directory structure that looks like:

```
cat.txt
hat.txt
dog.txt
images/
    cat.png
    hat.png
    dog.png
```

If the following pairs of commands are equivalent.

```bash
rm *.txt
rm cat.txt hat.txt dog.txt

rm ?at.txt
rm cat.txt hat.txt

rm **/hat.*
rm hat.txt images/hat.png

touch {mouse,house}.{txt,md}
touch mouse.txt mouse.md house.txt house.md
```

## Manual

There is a command `man` which will give you the **manual page** for any command.

```bash
man COMMAND
```

Use this to learn about all of the settings for the following commands.

## Text Commands

Text is the base data the shell works with.
Thus, there are tons of commands for manipulating and showing text.
That, combined with piping can get a lot done.

### Less

**Less** is a command that stores its input and lets you scroll through it.
If you have a command that just flushes a ton of text by the screen, you can use it.

```bash
ls | less
```

When you run `git log` or `man`, it automatically uses `less` as a **pager**.

#### Less Commands

When you see a colon `:` in the lower left, you can run commands.

* `q` quit
* `/` search forward
* `?` search backward
* `n` next search match
* `N` previous search match
* `C-n` next line, like `down`
* `C-p` previous line, like `up`
* `C-v` next page
* `M-v` previous page
* `M-<` beginning of input
* `M->` end of input

### Grep

**Grep** is for finding within files.
You should single quote `'` the pattern so that it isn't escaped by the shell itself.
The command you should use is `egrep` which turns on ["extended" POSIX regular expressions](https://en.wikibooks.org/wiki/Regular_Expressions/POSIX_Basic_Regular_Expressions) which act more like those you're used to.

```bash
egrep PATTERN FILES...
```

```bash
egrep -n '^SOME_CONST' *.py
ls | egrep -i 'word'
git log | egrep -iC 'settings'
```

Common Flags:

* `-C` print surrounding (context) lines
* `-n` print line numbers before each match
* `-i` case insensitive

### Other Text Commands

Most commands that take input also can take a list of file names as command arguments.
Use `cat` otherwise.

* `cat FILES...` print files
* `echo ONE TWO...` print command arguments; useful for shell prototyping
* `head` first few lines of input
* `tail` last few lines of input; `-f` to keep watching for new data (follow)
* `fex 'DELIMITER_INDEX'` [flexible field extractor](http://www.semicomplete.com/projects/fex)
* `wc` word (and line and character) count of input
* `sort` sort input
* `shuf` randomly shuffle input by lines
* `sort | uniq` uniqe lines of input
* `diff FILE_ONE FILE_TWO` show differences between two files
* `PIPELINE_READING_FILE | sponge FILE` [overwrite a file with a pipeline](https://joeyh.name/code/moreutils/)

Fancy, but super useful:

* `sed` [stream editor](http://www.grymoire.com/Unix/Sed.html)
* `jq` [JSON querier](https://stedolan.github.io/jq/)
* `mlr` [CSV querier](http://johnkerl.org/miller/doc/)

## Other Commands

* `z DIR_SUBSRT` [jump to a directory by most used](https://github.com/rupa/z/)
* `open FILE` open a file as if you went there in the Finder (macOS only)
* `xargs` run a command multiple times slotting in arguments
* `which COMMAND` show the full path to a command executable
* `find . -name 'GLOB'` find all files in the current directory matching a glob pattern
* `lsof` list all open files and network ports by program
* `watch COMMAND` repeatedly run a program and show output
* `strace` / `dtrace` see a program read and write files
