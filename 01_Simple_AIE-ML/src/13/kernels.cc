/*
* Copyright (C) 2025 Florent Werbrouck. All Rights Reserved.
* SPDX-License-Identifier: MIT
*/
/* A simple kernel
 */
#include <adf.h>
#include "include.h"
#include "aie_api/aie.hpp"

static int16_t TEST=1;
const int16_t coeff[16] = { 1, 1, 0, 0, 1, -1, 0, 0, 0, 0, 1, 1, 0, 0, 1, -1};

void simple(adf::input_buffer<cint16> & in, adf::output_buffer<cint16> & out) {

  aie::vector<int16, 16> data_int;
  aie::vector<int16, 16> coeff_block;
  aie::vector<int16, 16> data_int_o;


  auto data_i = aie::begin_vector<8>(in);
  auto data_o = aie::begin_vector<8>(out);

  aie::mmul<4, 4, 4, int16, int16> matrixMul;

  if(TEST==1)
  {
    TEST++;
  }

  coeff_block = aie::load_v<16>(coeff);

  for (unsigned i=0; i<NUM_SAMPLES/8; i++) {
      data_int = aie::vector_cast<int16>(*data_i++);
      matrixMul.mul(data_int, coeff_block);
      data_int_o = matrixMul.to_vector<int16>(0);
      *data_o++ = aie::vector_cast<cint16>(data_int_o);
  }
}
