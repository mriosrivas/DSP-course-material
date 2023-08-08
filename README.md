# DSP Course Material

Coursework material for DSP course thaught by Manuel Rios at the Universidad Rafael Landivar.

This is a series of Jupyter Notebooks aimed to learn Digital Signal Processing using Python. Each week you will have a different topic to work on and in between two main projects that will be assigned during the coursework.

## Week 1: Introduction

* Usage of Jupyter Notebooks
* Python, NumPy, Matplotlib and Pandas

## Week 2: Statistics

* Calculate signal statistics
* Implement running statistics
* Difference between histogram and probability mass function (PMF)
* Apply kernel density estimation

## Week 3: Decompositions

* Apply common decompositions to a signal

## Week 4: Convolution

* Implement convolution on time domain signals
* Accelerate convolution using matrix operations
* Implement convolution on images
* Develop correlation algorithm
* Use Barker's codes

## Week 5: Running Sum and First Difference

* Calculate firs difference and running sum
* Use your smartphone sensors

## Week 6: Fourier Transform

* Implement Fourier Transform and it's corrections
* Develop Inverse Fourier Transform
* Use frequency domain representation to filter a signal

## Week 7: Complex Fourier Transform and Fast Fourier Transform

* Implement the Complex Fourier Transform
* Implement the Complex Inverse Fourier Transform
* Deploy the FFT

## Week 8: Project: LMS filter and ADALINE algorithm

* Implement an LMS filter and ADALINE algorithm
* Test different learning rates
* Effects of overfitting on frequency and time domaing

## Week 9: IIR Digital Filter Design

* Plot zeros and poles of a filter
* Implement a narrow band filter using the zero pole placement method
* Implement a Chebyshev Direct II Transposed filter

## Week 10: FIR Filter -Moving Average

* Implement moving average filter by convolution and recursion
* Estimate the moving average of the crypto market

## Week 11: FIR Filter -Windowed-Sinc Filters

* Implement a low pass windowed sinc filter
* Implement a high pass spectral reversal filter
* Implement a high pass spectral inversion filter    
* Create a band pass filter using windowed filters

## Week 12: Project: Rock vs Metal

* Create and FM chirp signal
* Find the power spectral density using Bartlett's periodogram
* Create a classifier using a linear regression model

## More information:

* [Calendar - Google Drive](https://docs.google.com/spreadsheets/d/e/2PACX-1vRtuxRoc4WAkxlhIIzUuHW4ldcrHZxXXcQajIC32d89g5fT3zGkVJ2Z8BlP5DMcwBgDnI9j1PuEGoY2/pubhtml)
* [Shareable Online Calendar and Scheduling - Google Calendar](https://calendar.google.com/calendar/u/0?cid=NXRjcWJoOThtODM5NG8yNGQ0cDRhZm1rYm9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
* ## Running Using Docker:

You can use a Docker container to run all the Jupyter notebooks by doing the following steps:

1. Pull the anaconda3 container
   
   ```bash
   docker pull continuumio/anaconda3
   ```

2. Set an environment variable with the path where your repository was cloned. For example, if the repository was cloned on `/home/user/Documents`, the you will write
   
   ```bash
   LOCAL_PATH=/home/user/Documents
   ```

3. Run the container
   
   ```bash
   docker run -i -t -p 8888:8888 --volume {$LOCAL_PATH}/DSP-course-material:/DSP-course-material \
       continuumio/anaconda3 /bin/bash -c "\
       conda install jupyter -y --quiet && \
       mkdir -p /DSP-course-material && \
       jupyter notebook \
       --notebook-dir=/DSP-course-material --ip='*' --port=8888 \
       --no-browser --allow-root"
   ```

Check this [link](https://hub.docker.com/r/continuumio/anaconda3) if you need more information on how to use this container.
