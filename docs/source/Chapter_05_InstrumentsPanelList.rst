5. Instruments Panel List
==========================

Instruments Panels List (IPL) serves as an overview of all your instrument, and as a launchpad for a dedicated Instrument Tool Windows for each instrument:

Example of the IPL:

.. image:: images/instrument_panel_list.png

Description of the controls:

1. **SCPI Logger Toggle** - opens/closes SCPI Logger Tool Window. It logs the entire communication with your instrument coming from the plugin, and optionally your python script (for that, you need to switch on logging to UDP - see the `RsInstrument Logging help <https://rsinstrument.readthedocs.io/en/latest/StepByStepGuide.html#logging>`_).
2. **Open Instrument Tool Window** - opens dedicated Instrument Tool Window (ITW) with all the functions for the instrument. See the :ref:`6. Instrument Tool Window`.
3. **Test Connection** - tests, whether the connection to your instrument can be established. The connection is closed afterwards.
4. **Configure Instrument** - Opens the instrument's configuration dialog described in :ref:`adding-your-first-instrument`.
5. **Remove Instrument** - removes the instrument from the list.

.. tip::
    You can adjust the order by drag-and-drop:

    .. image:: images/instrument_list_drag_drop.png

.. tip::
    Adjust the look and feel in General Plugin Settings:

    .. image:: images/general_settings_invoke.png

    |

    .. image:: images/plugin_settings_instr_panels.png

    |

    This makes your list having this compact style:

    .. image:: images/instrument_panel_list_compact.png

.. tip::
    You can reach all the functionalities (and some more) through the context menu - right-click on the instrument picture. Now, select the **Open in dedicated Window** or press 'Q'

    .. image:: images/instrument_panel_context_menu_open_itw.png

    |

    **Open in dedicated Window** is only available if you have made at least one successful connection to your instrument, because the plugin needs to know the instrument's identification string.
