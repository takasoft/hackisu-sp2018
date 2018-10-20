import scipy.io
data = scipy.io.loadmat('eeglab_data.set')
data = data['EEG']
print(data.shape)
print(data)