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
gen_input:
	cd ./python; \
	python3 fft_gen.py
	
vitis_workspace:
	vitis -s create_workspace.py ${DEVICE_NAME} ${VERSION}
	
verif_output:
	cd ./python; \
	python3 verify_fft_out.py

ifeq ($(VERSION),1)
all: vitis_workspace
else ifeq ($(VERSION),2)
all: gen_input vitis_workspace
else
all: gen_input vitis_workspace 
endif
	
	
clean:
	rm -rf .Xil $(WORKSPACE_DIR) _ide aie/data
