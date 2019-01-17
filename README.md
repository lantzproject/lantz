Lantz: Simple yet powerful instrumentation in Python
====================================================

Lantz is an automation and instrumentation toolkit with a clean, well-designed
and consistent interface.  It provides a core of commonly used functionalities
for building applications that communicate with scientific instruments allowing
rapid application prototyping, development and testing.

The package is name lantzdev (not lantz) to avoid name collision with previous 
package.


Installing
----------

You can install the full version very easily:

    pip install -U "lantzdev[full]"

All requirements will be automatically installed for you except PyQt. 

We suggest  that you use [Anaconda Python Distribution](https://www.anaconda.com/) 
and use an environment
  
    conda create --name lantz python=3.6 pyqt
    
    conda activate lantz


Having fun
----------

If you do not have the NI-VISA library installed, install the pure python
replacement by running the following command in your terminal:

    pip install pyvisa-py    

and then tell Lantz to use it:

    lantz config core.visa_backend @py

Then start the simulator in one terminal:
    
    lantz sims fungen tcp
    
and the testpanel in another:
    
    lantz qtdemo testpanel



Installation options
--------------------

Lantz is organized ina modular way. You can install what you need.


### Minimal

If you just want to control instruments, simulate devices and create you own drivers.

    pip install -U lantzdev
    
subpackages used: *core, drivers, sims*

    
### Arduino 

If in aditional to **Minimal** you want to build arduino drivers.
    
    pip install -U "lantzdev[ino]"
    
- subpackages used: *core, drivers, sims, ino*

- suggested dependencies: *[arduino-cli](https://github.com/arduino/arduino-cli)*

    
### Qt 

If in aditional to **Minimal** you want to build arduino drivers.
    
    pip install -U "lantzdev[qt]"

- subpackages used: *core, drivers, sims, qt*

- required dependencies: *[PyQt > 5](https://riverbankcomputing.com/software/pyqt/intro)*


#### Full

    pip install -U "lantzdev[qt]"


- subpackages used: *core, drivers, sims, ino, qt*

- required dependencies: *[PyQt > 5](https://riverbankcomputing.com/software/pyqt/intro)*

- suggested dependencies: *[arduino-cli](https://github.com/arduino/arduino-cli)*


#### Install from git

You can try the latest version by installing from git. On your terminal:

    pip install -U https://github.com/lantzproject/lantz-core/zipball/master
    pip install -U https://github.com/lantzproject/lantz-drivers/zipball/master
    pip install -U https://github.com/lantzproject/lantz-qt/zipball/master
    pip install -U https://github.com/lantzproject/lantz-sims/zipball/master
    pip install -U https://github.com/lantzproject/lantz-ino/zipball/master
    pip install -U https://github.com/lantzproject/lantz/zipball/master
