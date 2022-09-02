12. Plugin Settings
=========================

Here, you can find all the general settings (non-instrument specific) for the plugin.
You can invoke it either from the :ref:`Main Instrument Panel<main-instrument-panel>`,
or the Pycharm menu *File -> Rohde & Schwarz IC Settings*.

12.1 General settings
"""""""""""""""""""""""""""""""""""""""

Contains general settings for the plugin, plus import/export features for stored data.

.. image:: images/plugin_settings_general.png

Description of the controls:

1. **Check for RsInstrument Python package** - when check, the plugin checks for the updates of the RsInstrument package. This only happens, during the IDE start, but if it takes a longer time, you can disable the checking.
2. **Show Editor Context Menu Item: Show Cmd Definition** - allow for this entry in the script editor right-click context menu.
3. **Show Editor Context Menu Item: Search Command** - allow for this entry in the script editor right-click context menu.
4. **Show Add Instrument Button at the Top** - showing the Add Instrument button on the top of the main panel is handy, if you have too many instruments in the list. Having the add button at the top saves you the scrolling down action.
5. **Export Plugin Settings** - Exports selected plugin settings, which you can transfer to another computer, or make a backup.
6. **Import Plugin Settings** - Imports the selected xml file as a plugin setting. You need to restart the Pycharm afterwards.


12.2 Instrument Panels
"""""""""""""""""""""""

Settings related to the *look-and-feel* of the Instrument Panel List (IPL).
The chapter :ref:`Instrument Panel List<5. Instruments Panel List>` shows how you can use the list and change the order or items.

.. image:: images/plugin_settings_instr_panels.png

Description of the special controls:

1. **Instruments Icon Size** - Change the icon size either with the slider or by entering the direct number.
2. **Maximum Description Length per Row** - limits the description width, so your panel can be compact in width. Use this to prevent e.g. long Resource Name strings to hide the action buttons.
3. **Easy Remove Mode** - If checked, removing an instrument from the list works with one click without a confirmation. Also, the remove icon is visible even for collapsed panels.

Other checkbox fields names correspond to the Instrument Panel elements. The changes have immediate effect, so you can see how your instruments list will look like.


12.3 Instrument Tool Windows
"""""""""""""""""""""""""""""

Common settings for all the ITWs.

.. image:: images/plugin_settings_itw.png

Description of the controls:

1. **Instruments Icon Size** - change the ITW header icon size.
2. **Enable All Function Panels** - overrides the internal table with the information which instrument supports which feature, and enables all the function panels. Use this on your own risk...
3. **VISA Timeout in ms for SCPI Tree reading** - maximum time the plugin waits for the instrument's response when reading the SCPI Tree. You can adjust it higher if your instrument needs more time to respond.
4. **VISA Timeout in ms for File Browser reading** - maximum time the plugin waits for the instrument's response when performing File Browser operations. You can adjust it higher if your instrument needs more time to respond.
5. **Temporary Folder for Instrument Files** - when you operate the File Browser, all the files copied from the instrument are stored in this path. We recommend to check the occupied size and clear this folder from time to time.
6. **Folder with Macro Script Files** - in this folder, all the macro scripts are stored. Change it to your liking.

.. _settings-scpi-code-completion:

12.4 SCPI Code Completion
""""""""""""""""""""""""""

Settings related to SCPI auto-completion.

.. image:: images/plugin_settings_scpi_code_completion.png

Description of the controls:

1. **Master Switch** - switches the complete SCPI Tree code completion ON or OFF.
2. **Suggestion Mode** - only has effect if the Instrument Tool Window (ITW) is active. If the ITW is inactive, the suggestion mode is always **All Commands**.

    - **All Commands** - always suggest all the available commands.
    - **Selected Group** - suggest only the commands from the currently selected group. If the instrument does not support group commands, this mode has the same effect as **All Commands**.
    - **Filtered Commands** - only suggest the commands that are currently visible in the SCPI Tree Function panel, also taking Filter feature into account.

3. **Chained Auto-popups** - when the SCPI commands suggestion starts, the suggestion popups are invoked automatically until the command is completed.
4. **Update ITW Search Field** - as the auto-completion composes the SCPI command, the :ref:`Find Field 5 in the ITW SCPI Tree<7. Function Panel - SCPI Tree>` is updated, which triggers the SCPI Tree item navigation.
5. **Threshold for Full Commands List** - as you are completing the SCPI command, the amount of the possible suggestions decreases. When it falls below this threshold, the suggestions will contain not only the next header, but the full command up to the end.
6. **Default Instrument for SCPI Tree** - there are cases, where you are might use script variables that do not fit any of your instrument's aliases. Such case is for example a common sub-routine serving more than one instrument. If you still want to use the SCPI code completion, you have to tell the RSIC plugin which SCPI Tree to use. You can do it here by defining a default instrument.

12.5 Code Inspections
""""""""""""""""""""""

Settings affecting code inspections. Currently only one feature is supported.

.. image:: images/plugin_settings_code_inspections.png

Description of the controls:

1. **Disable Typo Errors for SCPI Strings** - removes the distracting green underlines for all the SCPI strings which highlight typo errors. The typo checking still works for other parts of your script.

.. _settings-templates:

12.6 Templates
""""""""""""""""""""""

All the snippets pasted into your script can be adjusted here. The Templates are split into 4 groups: General, Write, Query, File
General, Write and Query templates are used by the SCPI Communicator to import package, create the constructors, write and query commands.
File Templates are used by the File Browser to insert code snippets for reading / writing files to the instrument.

.. image:: images/plugin_settings_templates.png