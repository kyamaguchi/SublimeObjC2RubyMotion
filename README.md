# ObjC2RubyMotion Converter for Sublime Text 2

A command plugin that enables to convert Objective-C code to Ruby Motion.

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

### Conversions

In internal order

* Replace NSString `@"String"` -> `"String"`
* Convert square brackets expression  `[[Obj alloc] init]` -> `Obj.alloc.init`
* Remove semicolon `;` at the end of line
* Remove `autorelease` at the end
* Remove type declaration for Object `Type *` before `=`

## Install

### Package Control
Install the `ObjC2RubyMotion` package from [Package Control](http://wbond.net/sublime_packages/package_control).


### Manual

Clone this repository from your Sublime packages directory:

#### Macosx

```
$ cd "~/Library/Application Support/Sublime Text 2/Packages"
$ git clone https://github.com/kyamaguchi/SublimeObjC2RubyMotion.git ObjC2RubyMotion
```

## Key Binding

By default,

For Conversion

`super+ctrl+i` `objc_to_ruby_motion`

For Running unit test

`super+shift+ctrl+t` `show_objc_to_ruby_motion_tests_suites`

## Tests

Fortunately ObjC2RubyMotion has tests.

Run the command `show_objc_to_ruby_motion_tests_suites`

and Enter(`objc_to_ruby_motion` test suite will run).
