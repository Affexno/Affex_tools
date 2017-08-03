import os

def _write_uti():
        core = ('/tmp/hdump/') # Change this depending on where you want to store your files.
        ext = ('.uti')
        
        if not os.path.exists(core):
                os.makedirs(core)
        
        if len(hou.selectedNodes()) < 1: # Error out if nothing is selected.
            hou.ui.displayMessage("Nothing selected!")
        else:
            name_dump = hou.ui.readInput('Name file!', title="Name input here.")
            name = name_dump[1]
            nodes = hou.selectedNodes()
            
            path = core + name + ext

            # Write files.
            parent = nodes[0].parent()
            if not all(node.parent() == parent for node in nodes):
                raise Exception("Nodes must have the same parent.")

            parent.saveItemsToFile(nodes, path)

_write_uti()
