# ObjC2RubyMotion Converter for Sublime Text 2/3

A command plugin that enables to convert Objective-C code to Ruby Motion.

### Screenshot:

![screenshot](https://raw.github.com/kyamaguchi/SublimeObjC2RubyMotion/master/screenshot.gif)

_Using iShowU, KeyCastr, GIFBrewery_

## How It Works

Code in the line of the cursor or selection are converted:

```objc
// original
_window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
self.window.rootViewController = self.myNavController;
[self.window makeKeyAndVisible];

// select lines and run "objc_to_ruby_motion"
_window = UIWindow.alloc.initWithFrame(UIScreen.mainScreen.bounds)
self.window.rootViewController = self.myNavController
self.window.makeKeyAndVisible
```

## Install

### [NOT available yet] Package Control
Install the `ObjC2RubyMotion` package from [Package Control](http://wbond.net/sublime_packages/package_control).


### Manual

Clone this repository from your Sublime packages directory:

#### Macosx

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
$ git clone https://github.com/kyamaguchi/SublimeObjC2RubyMotion.git ObjC2RubyMotion
```

## Key Binding

By default,

For Conversion

`super+ctrl+i` `objc_to_ruby_motion`

## Conversions

#### In internal order

* Replace NSString `@"String"` -> `"String"`
* Convert blocks (may be not perfect)
* Convert square brackets expression  `[[Obj alloc] init]` -> `Obj.alloc.init`
* Remove semicolon `;` at the end of line
* Remove `autorelease` at the end
* Remove type declaration for Object `Type *` before `=`

#### NOT supported

* if else conditions etc.
* YES/NO
* actions `action:@selector(tapped:)`
* Method name and args conversion `- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section`
* Others

#### Note

This converter is not intended to convert perfectly. This is intended to help the conversion of Objective-C code snippets.

Some complex expression may not be converted correctly.

## Tests

:smile: Fortunately ObjC2RubyMotion has tests.

### Run test from command line

```
$ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/ObjC2RubyMotion
$ python tests/all_test.py
```

OR

:racehorse: Use guard

```
# Requirement: ruby
$ gem install guard
$ gem install guard-shell
$ guard
```

## Customize

1. Fork it

2. Remove original ObjC2RubyMotion and clone yours OR add your repository as another git remote

  ```
  $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
  $ git clone git@github.com:yourname/SublimeObjC2RubyMotion.git ObjC2RubyMotion
  ```

3. Copy test file and write new test

  `cp tests/test_basic.py tests/test_custom.py`

4. :snake: Change and Test

  Normally, you should change `CodeConverter.py` and `test_*.py`.

  `$ guard` is recommended.

#### Note

Probably most users of this plugin are rubyist, not pythonista.

This converter is mostly composed of regular expression for now.

If we try to improve this to convert more complex expressions, probably we need to replace the converter with the one using parser/tokenizer/scanner.

Fork is welcomed.

Care about unexpected string replacements. They could happen and they will be problems.
