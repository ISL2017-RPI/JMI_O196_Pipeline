import sys
import JMI_O196
import numpy as np

def JMI(data_file, target_file, hm_feat):
    my_JMI = JMI_O196.initialize()
    feat = my_JMI.JMI_primitive_O196(data_file, target_file, hm_feat)
    return feat


if __name__ == "__main__":
    data = 'trainData.csv'
    target = 'trainTargets.csv'
    hm_feat = 5
    selected_feature = np.array(JMI(data, target, hm_feat), dtype=np.int16)
    np.savetxt('Features_O196_JMI.csv', selected_feature, delimiter=',')
    print selected_feature