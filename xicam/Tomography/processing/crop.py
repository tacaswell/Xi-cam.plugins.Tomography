from xicam.plugins import ProcessingPlugin, Input, InOut
import numpy as np


class Crop(ProcessingPlugin):
    recon = InOut(description='Array to crop along given access (slicing)', type=np.ndarray)
    p11 = Input(description='First point along first axis', type=int)
    p12 = Input(description='Second point along first axis', type=int)
    p21 = Input(description='First point along second axis', type=int)
    p22 = Input(description='Second point along second axis', type=int)
    axis = Input(description='Axis to crop along', type=int, default=0)

    def evaluate(self):
        slc = []
        pts = [self.p11.value, self.p12.value, self.p21.value, self.p22.value]
        for n in range(len(self.recon.value.shape)):
            if n == self.axis.value:
                slc.append(slice(None))
            else:
                slc.append(slice(int(pts.pop(0)), -int(pts.pop(0))))
        self.recon.value = self.recon.value[slc]
