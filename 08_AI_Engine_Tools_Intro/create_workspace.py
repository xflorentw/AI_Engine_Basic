#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#

import vitis
import sys
import os


part=sys.argv[1]
workspace="workspace"

app_path= os.getcwd()

client = vitis.create_client()
client.set_workspace(path=workspace)

# Create AIE-ML component
print ("\n-----------------------------------------------------")
print ("Creating AIE-ML component from Simple template\n")
comp = client.create_aie_component(name="aie_component_simple", part = part, template = "installed_aie_examples/simple")
comp = client.get_component(name="aie_component_simple")

vitis.dispose()