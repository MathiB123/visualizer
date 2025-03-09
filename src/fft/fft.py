from numpy.typing import ArrayLike

def power_of_2_fft(fs: ArrayLike):
    assert(len(fs).bit_count() == 1) #Is a power of 2

    