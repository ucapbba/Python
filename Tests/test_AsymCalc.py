from Source.MachineLearning.ARC.ImageClassifierHelper import ImageClassifierHelper


def test_GetValuesFromFilename():
    somePath = "somePath"
    filename = "Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat"
    helper = ImageClassifierHelper(somePath, filename)
    values = helper.GetValuesFromFilename()
    Idiff = values.Idiff
    w2 = values.w2
    phi = values.phi
    assert w2 == str(1)
    assert Idiff == str(1000)
    assert phi == str(0.025)


def test_IsAmplitudeGrid():
    somePath = "somePath"
    filename = "Amplitude_Grid_w2_1_1000_phi_0.025_750X750.dat"
    helper = ImageClassifierHelper(somePath, filename)
    assert helper.IsAmpGrid()
    filename = "random_name"
    helper = ImageClassifierHelper(somePath, filename)
    assert not helper.IsAmpGrid()
