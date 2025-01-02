Version 3.6.1 - 13.12.2024
	- Fixed not working SCPI code completion in SCPI Fields and SCPI Editors.

Version 3.6.0 - 05.12.2024
	- Reworked Templates system - now you can also generate C#, MATLAB, or custom language code.
	- Added History of Resource Names in the Instrument Configuration Window.
	- Reworked and improved Copy-Paste-Drag/Drop behaviour. Paste Special Context menu allows for pasting SCPI with different options.
	- Examples of SCPI Write/Query commands now also include parameters, even the complex ones.
	- Added SFI instrument.
	- Added C# code SCPI Parser.
	- Fixed NRX Screenshot and File Browser for Firmware > 2.61.
	- Fixed SCPI Files annotations for inactive instruments.
	- Added SFI instrument.
	- Improved NI IO VISA Trace Parser for German language.
	- Fixed GUI behaviour when changing the theme.
	- Added session interface type symbols to instrument icons (switchable).
	- In the Instrument configuration: added history for LAN IP Address, USB PID,VID,SN, Custom Resource Name.
	- Added copy/paste of single instrument in the instrument's list.
	- Fixed \0 appearance in the SCPI parser results.
	- Fixed SCPI Editor Controls for master/second File Editors.

Version 3.5.0 - 23.09.2024
	- Added EPL instrument.
	- Added SCPI Recorder for ZNB.
	- Improved inlays behaviour when editing the SCPI File.
	- Added hint for SCPI Searcher in Multi-Line SCPI Editor.
	- Instrument Config Window: added button to directly open the Instrument Tool window.
	- Instrument Config Window: Added checking for similar existing instruments.
	- Added simple simulation instrument configuration with CTRL+Add Instrument.
	- Under the hood: updated org.jetbrains.intellij to 2.0.1.
	- Under the hood: updated Java RsInstrument to 1.9.0.

Version 3.4.0 - 02.07.2024
	- Version for Pycharm 2024.1.x, and newer.
	- New: File Browser ITW now allows recursive folder reading.
	- New: SCPI Editor has graphic bars displaying command execution time.
	- New: SCPI Editor now offers pause + pause-on-error function.
	- New: SCPI Editor has new meta commands for switching error checking ON/OFF.
	- NEW: SCPI Parser for R&S Elektra Logs.
	- NEW: SCPI Parser for FormFactor Logs.
	- New: Instrument communicator panel has option to add Go-To-Local / Remote + Error checking buttons to the toolbar.
	- Updated all instrument pictures.
	- Improved checks for instrument names.
	- Fixed many ETD / BGT framework exceptions.
	- Under the hood: updated org.jetbrains.intellij to 2.0.0.

Version 3.3.0 - 17.06.2024
	- Version targeted for Pycharm branch 2024.1.x. For 2024.2.x, there will be a version 3.4.0.
	- Added NGC, NPA, HMC8012 and HMC8015 instruments support - pictures + SCPI Trees
	- Improved NRP-Zxx instruments configuration - ambiguity between the 'RSNRP::' and 'USB::0x0AAD'
	- Fixed: EDT Exception in 'Search for Instruments' dialog window.
	- Fixed: HelloWorld script naming bug.
	- Under the hood: updated Java RsInstrument to 1.7.0 with logger.

Version 3.2.0 - 26.04.2024
	- Fixed compatibility with Pycharm 2024.1.x.
	- Added CMW100 Picture and instrument recognition.
	- Corrected known USB instruments - NRPxxS/N.
	- Fixed LCX File Browser - changed home path and root path.
	- Added CMA180 Web-Help. You need to be logged in with your R&S Gloris account
	- Fixed 'Paste to SCPI Text Field' caused by missing package on the target 2024.x Pycharm version.
	
	- Under the hood: updated org.jetbrains.intellij to 1.17.3

Version 3.1.0 - 31.03.2024
	- Added Curves Function panel to conveniently querying traces, waveforms and other array data.
	- Added pre-defined curves to 3 different instrument groups: SignalAnalyzer, VectorSignalAnalyzer, Oscilloscope.
	- Added support for M3SR radios - new Instrument Profile 'XK41'.
	
	- Fixed NI VISA Parser where it ignored certain write commands.
	- Fixed bug with Instrument List when you opened second project.
	- Fixed ZNL SCPI Tree Groups.
	- Fixed multiple Event Dispatch Thread exceptions.
	- Fixed proper sorting of SCPI Groups with different priorities.

	- Under the hood: updated JRsInstrument to 1.6.0.

Version 3.0.0 - 02.02.2024
	- Removed support for Pycharm older than 2023.3.
	- Partial support for New UI.
	- New Instruments List Toolbar for Actions and Filter.
	- GUI toolbars changed to standard Intellij Action Toolbars.
	- Fixed Instrument Tool Window Tabs where clicking directly on the icon did not work.
	- Fixed many instances of non EDT-invoke exceptions due to the changes in the Intellij framework.
	- Advanced SCPI Parser - improved performance and removed the reparse/auto-parse buttons. Added SMx Web Log Format recognition.
	- Under the hood: updated org.jetbrains.intellij to 1.17.2, JRsInstrument to 1.5.0.

Version 2.1.1 - 18.12.2023

	- Fixed compatibility with Pycharm 2023.3.x

Version 2.1.0 - 23.10.2023

	- Corrected toggle and action buttons in New UI.
	- Updated Pulse Sequencer SCPI Tree.
	- Added SCPI code-completion for commands with simple array parameters.
	- Improved error message when no VISA is installed.
	- Added history function for Instrument List filter box.

Version 2.0.0 - 21.09.2023

	- Removed compatibility with Pycharm 2022.x.
	- Full integration of SCPI Language, including new SCPI Editor with customizable color schemes.
	- SCPI Multi-liners are now native SCPI Editors with the capability of controlling multiple instruments.
	- Template for SCPI files: Use the ProjectTree -> Project right-click -> New -> SCPI File.
	- Added advanced SCPI parser - very useful for IO Traces.
	- Fixed Communicator Write/Query functions.
	- Fixed Communicator waiting Timeout.
	- All VISA sessions are closed on Pycharm exit.
	- Under the hood: updated org.jetbrains.intellij to 1.15.0, RsInstrument to 1.4.4

Version 1.3.1 - 11.04.2023

	- Added compatibility with Pycharm 2023.1+

Version 1.3.0 - 01.02.2023

	- Added compatibility with Pycharm 2022.3.1+
	- Fixed error with calling VISA native DLLs in Pycharm version 2022.3.1+
	- Added option to create a Hello-World Python script.
	- Improved FSW SCPI Recorder, added SigGens SCPI Recorder.
	- Added multi-line window for plain SCPI commands editing and execution.
	- Multi-line window has a powerful SCPI parser from different text and log formats.
	- Reworked and unified SCPI Drag & Drop actions.
	- SCPI Tree: FSW now has an option to change drives.
	- Connect Button: added menu item 'Set Error Checking ON/OFF'.
	- Under the hood: updated org.jetbrains.intellij to 1.12.0


Version 1.2.0 - 21.12.2022

	- Added compatibility with Pycharm 2022.3.
	- Added 1st version of FSW SCPI Interactive Recorder.
	- Added VNC, RDP, Web-Control quick launch buttons.
	- Added one-click to open the instrument's website (for LAN sessions).
	- Added option to import settings XML file from the previous Pycharm Version.
	- Fixed text wrapping in the SCPI Communicator for ASCII and BINary responses.
	- Fixed SMA100B File Browser.
	- Under the hood: updated org.jetbrains.intellij to 1.10.1, RsInstrument to 1.4.1


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