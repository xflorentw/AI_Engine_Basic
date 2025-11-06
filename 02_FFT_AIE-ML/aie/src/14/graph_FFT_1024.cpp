/*
* Copyright (C) 2025 Florent Werbrouck. All Rights Reserved.
* SPDX-License-Identifier: MIT
*/
#include <adf.h>
#include "graph_FFT_1024.h"

using namespace adf;

my_graph mygraph;

#if defined(__AIESIM__) || defined(__X86SIM__)

int main(void) {
  mygraph.init();
  mygraph.run(1);
  mygraph.end();
  return 0;
}

#endif
