import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
from colour import Color
import numpy as np


class PiOrbit :

    def __init__(
        self : object,
        n : int,    # number of digits of pi
        k : float,  # the force constant
        c : float,  # coefficient of friction
        h : float,  # time step
        lim : float # radius of nearest approach
        ) :
        self.d = {
            '0' : 0.00000000000000,
            '1' : 0.62831853071795,
            '2' : 1.25663706143591,
            '3' : 1.88495559215387,
            '4' : 2.51327412287183,
            '5' : 3.14159265358979,
            '6' : 3.76991118430775,
            '7' : 4.39822971502571,
            '8' : 5.02654824574366,
            '9' : 5.65486677646162
            }
        self.frames = 0
        self.j  = 1    # jth digit of pi
        self.m  = 0    # mth point on path
        self.ds = 10   # distance between particle and digit
        self.h  = h    # timestep
        self.k  = k    # force constant
        self.c  = c    # friction coefficient
        self.lim = lim # radius of nearest approach
        self.x0  = np.cos( self.d[ '3' ] )  # initial x position
        self.y0  = np.sin( self.d[ '3' ] )  # initial y position
        self.xpos = np.array( [ self.x0 ] ) # x path
        self.ypos = np.array( [ self.y0 ] ) # y path
        self.pnts = [ ( self.x0, self.y0 ) ]
        self.segs = [] # each line segment
        self.segc = [] # color of each line segment
        self.v0x  = 0  # initial x velocity
        self.v0y  = 0  # initial y velocity
        self.prev = '' # previous value
        self.fig  = plt.figure()
        self.pi   = plt.imread( 'pi.png' ) # pi image
        self.spc  = plt.imread( 'space.jpg' ) # space image
        
        # reading n decimal digits of pi
        self.dgts = []
        with open( 'pi1mdigits.txt' ) as file :
            self.dgts = list( file.read( n ) )
        # creating colormap
        self.color = list(
            Color( 'purple' ).range_to( Color( 'red' ), 500 )
            )
        self.color += list(
            Color( 'red' ).range_to( Color( 'orange' ), 500 )
            )
        self.color += list(
            Color( 'orange' ).range_to( Color( 'yellow' ), 500 )
            )
        self.color += list(
            Color( 'yellow' ).range_to( Color( 'green' ), 500 )
            )
        self.color += list(
            Color( 'green' ).range_to( Color( 'blue' ), 500 )
            )
        self.color += list(
            Color( 'blue' ).range_to( Color( 'purple' ), 500 )
            )
        
    def animate( self : object, i : int ) -> None :
        # check to radius of nearest approach
        if ( self.ds <= self.lim and
             self.dgts[ self.j ] != self.prev ) :
            self.prev = self.dgts[ self.j ]
            self.j += 1
            if self.j >= len( self.dgts ) :
                return
        # position of charge
        th = self.d[ self.dgts[ self.j ] ]
        xn, yn = np.cos( th ), np.sin( th )
        # avoid singularity
        if self.dgts[ self.j ] != self.prev :
            # calculating new acceleration
            a0x = self.k*( xn - self.x0 ) /\
                  ( ( xn - self.x0 )**2 +
                    ( yn - self.y0 )**2 )**( 3/2 ) \
                  -self.c * self.v0x # friction
            a0y = self.k*( yn - self.y0 ) /\
                 ( ( xn - self.x0 )**2 +
                   ( yn - self.y0 )**2 )**( 3/2 ) \
                 -self.c * self.v0y # friction
        # avoid singularity
        else :
            if self.ds >= self.lim :
                self.prev = ''
            # shut off inverse square field
            a0x = -self.c * self.v0x # friction
            a0y = -self.c * self.v0y # friction
        # velocity and position
        v1x = self.v0x + a0x*self.h
        v1y = self.v0y + a0y*self.h
        x1  = self.x0 + v1x*self.h + 0.5*a0x*( self.h**2 )
        y1  = self.y0 + v1y*self.h + 0.5*a0y*( self.h**2 )
        # append to path and line segments
        self.xpos = np.append( self.xpos, [ x1 ] )
        self.ypos = np.append( self.ypos, [ y1 ] )
        self.segs.append( [ ( self.x0, self.y0 ), ( x1, y1 ) ] )
        plt.clf()
        # plotting labels
        lbl = 0
        for rd in self.d.values() :
            plt.text(
                np.cos( rd ),
                np.sin( rd ),
                str( lbl ),
                size = 10,
                color = 'white',
                verticalalignment = 'center',
                horizontalalignment = 'center',
                bbox = dict(
                    facecolor = 'black',
                    edgecolor = 'white',
                    boxstyle  = 'circle'
                    ),
            )
            lbl += 1
        # plotting particle
        plt.text(
            x1,
            y1,
            self.dgts[ self.j ],
            size = 10,
            color = 'white',
            verticalalignment = 'center',
            horizontalalignment = 'center',
            bbox = dict(
                facecolor = 'black',
                edgecolor = 'white',
                boxstyle  = 'circle'
                ),
        )
        # plotting path
        plt.plot(
            self.xpos,
            self.ypos,
            alpha = 0
            )
        ax = plt.gca()
        # plotting lines
        self.segc.append( self.color[ self.m % len( self.color ) ].rgb )
        ax.add_collection(
            LineCollection(
                segments = self.segs,
                linewidths = 0.5,
                colors = self.segc
                ),
            autolim = False
            )
        # plotting background
        ax.imshow(
            self.spc,
            extent = [
                -2.2, 2.2,
                -1.7, 1.7
                ]
            )
        # plotting pi image
        ax.imshow(
            self.pi,
            extent = [
                -0.25, 0.25,
                -0.25, 0.25
                ]
            )
        # adjusting parameters
        plt.subplots_adjust(
            top = 1, bottom = 0, right = 1,
            left = 0, hspace = 0, wspace = 0
            )
        plt.margins( 0,0 )
        ax.axis( 'off' )
        # set new values to previous values
        self.v0x = v1x
        self.v0y = v1y
        self.x0 = x1
        self.y0 = y1
        self.ds = np.sqrt( ( xn - self.x0 )**2 +
                           ( yn - self.y0 )**2 )
        self.frames += 1
        self.m += 1
        return

    def start( self : object ) -> None :
        anim = animation.FuncAnimation(
            fig = self.fig, func = self.animate, interval = 1, repeat = False, frames = 50000
            )
        plt.show()
        
