#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#

# =========================================================
# DEVICE SELECTION
# =========================================================
DEVICE_NAME ?= xcve2302-sfva784-1LP-e-S

##############
# Build Flow #
##############
all:
	vitis -s create_workspace.py ${DEVICE_NAME}
	
clean:
	rm -rf $(BUILD_DIR)
	rm -rf .Xil $(WORKSPACE_DIR) _ide