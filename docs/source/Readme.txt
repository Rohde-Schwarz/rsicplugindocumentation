Rohde & Schwarz Instrument Control Pycharm plugin (RsIC) is targeted for our customers that use Pycharm for writing python instrument remote-control scripts.
It is optimized, although not exclusive to be used with our `RsInstrument Python package <https://pypi.org/search/?q=rsinstrument>`_

User Manual: https://rsicpycharmplugin.readthedocs.io

Version history

Version 1.3.0 - 01.02.2023

	- Added compatibility with Pycharm 2022.3.1+
	- Fixed error with calling VISA native DLLs in Pycharm version 2022.3.1+
	- Added option to create a Hello-World Python script.
	- Improved FSW SCPI Recorder, added SigGens SCPI Recorder.
	- Added multi-line window for plain SCPI commands editing and execution.
	- Multi-line window has a powerful SCPI parser from different text and log formats.
	- Reworked and unified SCPI Drag & Drop actions.
	- SCPI Tree - FSW now has an option to change drives.
	- Connect Button - added menu item 'Set Error Checking ON/OFF'.
	- Under the hood - updated org.jetbrains.intellij to 1.12.0


Version 1.2.0 - 21.12.2022

	- Added compatibility with Pycharm 2022.3.
	- Added 1st version of FSW SCPI Interactive Recorder.
	- Added VNC, RDP, Web-Control quick launch buttons.
	- Added one-click to open the instrument's website (for LAN sessions).
	- Added option to import settings XML file from the previous Pycharm Version.
	- Fixed text wrapping in the SCPI Communicator for ASCII and BINary responses.
	- Fixed SMA100B File Browser.
	- Under the hood - updated org.jetbrains.intellij to 1.10.1, RsInstrument to 1.4.1


Version 1.1.1 - 19.10.2022

	- Changed GUIs to flat elements.
	- Added support for the new MXO Oscilloscope and CMQ500 Shielding cube.
	- Changed and improved instruments list filtering.
	- Improved SCPI code-completion.
	- Updated documentation.
	- SCPI Communicator - improved handling of timeout, error message shows directly in the response field.
	- SCPI Communicator - added automatic recognition of binary response.
	- SCPI Communicator - added option to have Write / Query buttons visible simultaneously.
	- SCPI Communicator - reworked History and added Favorite commands.
	- SCPI Tree Function Panel - improved SCPI Tree group names, added items to the context-menu.
	- SCPI Tree Function Panel - now it is possible to drag commands to your Python script.
	- Macros - added buttons rearrangement possibility, new macro for NGx instruments VNC enabling.
	- Templates - reworked handling single/double string quotes.
	- Fixed several bugs.
	- Fixed RTA/B/M Scpi Tree errors.
	- Various improvements.
	- Under the hood - updated org.jetbrains.intellij to 1.9.0, RsInstrument to 1.2.0


Version 1.0.1 - 01.09.2022

	First Released Version