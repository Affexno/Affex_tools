def getCurrentNetworkTab(self):
    network_tabs = [t for t in hou.ui.paneTabs() if t.type() == hou.paneTabType.NetworkEditor]
        if network_tabs:
            for tab in network_tabs:
                if tab.isCurrentTab():
                  return tab
        return None


exec_network = self.getCurrentNetworkTab() # Grab parent.

if not exec_network:
    hou.ui.displayMessage("No network tabs found to load into.", severity=hou.severityType.Error)

    file = hou.ui.selectFile(start_directory='/tmp/hdump/', title="Pick dump to import", collapse_sequences=False, )
    path = os.path.expandvars(file)
    parent = exec_network.pwd()

    # Load from selected file.
    parent.loadItemsFromFile(path)

   
