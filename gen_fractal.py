import matplotlib.pyplot as plt
import scipy.fft as sfft
import numpy as np
import numpy.random as rnd
rnd.seed()

def gen_fractal(N, D):
    D = 2.3
    beta = 2*(4. - D)
    ndim= int(N)
    N2  = int(ndim/2)

    data = np.zeros((ndim, ndim, ndim), dtype=complex)
    fndim = float(ndim)

    ix = 0
    while ix < N2:
        iy = 0
        while iy < ndim:
            iz = 0
            while iz < ndim:
                phi = rnd.uniform(0, 2.0*np.pi)
                fix = min(float(ix), float(ndim-ix))
                fiy = min(float(iy), float(ndim-iy))
                fiz = min(float(iz), float(ndim-iz))
                freq = np.sqrt(fix*fix + fiy*fiy + fiz*fiz)
                amp = np.sqrt(float(1.0/(freq/ndim)**beta))

                data[ix,iy,iz] = complex(amp*np.cos(phi), amp*np.sin(phi))
                iz += 1
            iy += 1
        ix += 1
    ix = 0
    while ix < N2:
        iy = 0
        while iy < ndim:
            iz = 0
            while iz < ndim:
                data[(ndim-ix)%ndim,(ndim-iy)%ndim,(ndim-iz)%ndim] = np.conj(data[ix,iy,iz])
                iz += 1
            iy += 1
        ix += 1
    data[0,0,0]=complex(0.0,0.0)
    data[0,0,N2]=complex(abs(data[0,0,N2]),0.0)
    data[0,N2,0]=complex(abs(data[0,N2,0]),0.0)
    data[N2,0,0]=complex(abs(data[N2,0,0]),0.0)
    data[0,N2,N2]=complex(abs(data[0,N2,N2]),0.0)
    data[N2,0,N2]=complex(abs(data[N2,0,N2]),0.0)
    data[N2,N2,0]=complex(abs(data[N2,N2,0]),0.0)
    data[N2,N2,N2]=complex(abs(data[N2,N2,N2]),0.0)

    ffdata= sfft.fftn(data)
    ffdata= sfft.fftshift(ffdata)

    var=np.var(ffdata)
    ffdata=ffdata/np.sqrt(var)

    fbmcube=np.sqrt(ffdata**2).astype('float64')

    h = np.std(fbmcube.flatten())
    dens= np.exp(fbmcube/h)

    (xind, yind, zind) = np.unravel_index(dens.argmax(), dens.shape)
    xroll = int(xind - N2)
    yroll = int(yind - N2)
    zroll = int(zind - N2)
    dens = np.roll(dens, -xroll, axis=0)
    dens = np.roll(dens, -yroll, axis=1)
    dens = np.roll(dens, -zroll, axis=2)

    return dens
