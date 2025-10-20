#
# Copyright (C) 2025, Florent Werbrouck. All rights reserved.
# SPDX-License-Identifier: MIT
#

WORKSPACE_DIR = workspace
# =========================================================
# DEVICE SELECTION
# =========================================================
DEVICE_NAME ?= xcve2302-sfva784-1LP-e-S

# =========================================================
# PARAMETERS
# =========================================================
VERSION ?=1

##############
# Build Flow #
##############
all:
	vitis -s create_workspace.py ${DEVICE_NAME} ${VERSION}
	
clean:
	rm -rf .Xil $(WORKSPACE_DIR) _ide