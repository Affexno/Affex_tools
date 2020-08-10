# ------------------AFFEX--2020---------------------------------------------------------
# Add Merge node to current network and wire them up.
# --------------------------------------------------------------------------------------

#Find the current network pane under cursor.
currNetworkPane = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.NetworkEditor)
currNode = currNetworkPane.pwd()

#Create merge node.
createdNode = currNode.createNode("merge")

#Get current position, create node.
cursorPos = currNetworkPane.cursorPosition()
createdNodePos = createdNode.position()
deltaPos = hou.Vector2((cursorPos[0] - createdNodePos[0])-0.5, (cursorPos[1] - createdNodePos[1])-0.5)

# Move to mouse position.
createdNode.move(deltaPos)

# Check if anything is selected. 
if len(hou.selectedNodes()) > 0:
    sel = hou.selectedNodes()[0]
    
    # Connect all nodes to merge node.
    for idx, node in enumerate(hou.selectedNodes()):
        createdNode.setInput(idx, node)
