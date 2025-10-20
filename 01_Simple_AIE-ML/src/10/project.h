/*
* Copyright (C) 2025 Florent Werbrouck. All Rights Reserved.
* SPDX-License-Identifier: MIT
*/
#include <adf.h>
#include "kernels.h"
#include "kernels/include.h"

using namespace adf;

class simpleGraph : public adf::graph {
private:
  kernel first;
  kernel second;
public:
  input_plio  in;
  output_plio out;
  simpleGraph(){
    
    in  = input_plio::create(plio_64_bits, "data/input_64.txt", 500);
    out = output_plio::create(plio_64_bits, "data/output.txt",500);

    first = kernel::create(simple);
    second = kernel::create(simple);
    adf::connect(in.out[0], first.in[0]);
    connect(first.out[0], second.in[0]);
    connect(second.out[0], out.in[0]);
    dimensions(first.in[0]) = { NUM_SAMPLES };
    dimensions(first.out[0]) = { NUM_SAMPLES };
    dimensions(second.in[0]) = { NUM_SAMPLES };
    dimensions(second.out[0]) = { NUM_SAMPLES };

    source(first) = "kernels/kernels.cc";
    source(second) = "kernels/kernels.cc";

    runtime<ratio>(first) = 1;
    runtime<ratio>(second) = 1;

  }
};
