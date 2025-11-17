/*
* Copyright (C) 2025 Florent Werbrouck. All Rights Reserved.
* SPDX-License-Identifier: MIT
*/
#include <adf.h>
#include "fft_ifft_dit_1ch_graph.hpp"

using namespace adf;

#define DATA_TYPE_FFT cint16
#define TWIDDLE_TYPE cint16
#define POINT_SIZE 1024
#define TP_FFT_NIFFT 1
#define TP_SHIFT 10

class my_graph : public graph {
public:
  input_plio in;
  output_plio out;
  
  xf::dsp::aie::fft::dit_1ch::fft_ifft_dit_1ch_graph<DATA_TYPE_FFT, TWIDDLE_TYPE, POINT_SIZE,TP_FFT_NIFFT,TP_SHIFT> fft_1024;

  my_graph() {
    in  = input_plio::create(plio_64_bits, "data/input.txt");
    out  = output_plio::create(plio_64_bits, "data/output.txt");

    connect<>(in.out[0], fft_1024.in[0]);
    connect<>(fft_1024.out[0], out.in[0]);
  }
};
