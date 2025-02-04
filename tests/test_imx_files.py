import pytest

from imxInsights import ImxSingleFile


@pytest.mark.slow
def test_imx_parse_project_v124(imx_v124_project_instance: ImxSingleFile):
    imx = imx_v124_project_instance
    assert imx.file.imx_version == "1.2.4", "imx version should be 1.2.4"
    assert len(list(imx.initial_situation.get_all())) == 5600, "objects in tree should is off"
    assert len(imx.initial_situation.get_build_exceptions()) == 0, "should not have no exceptions"
    assert len(list(imx.new_situation.get_all())) == 5725, "objects in tree should is off"
    assert len(imx.new_situation.get_build_exceptions()) == 0, "should not have no exceptions"


@pytest.mark.slow
def test_imx_multiple_same_extension_objects_v124(imx_v124_project_instance: ImxSingleFile):
    imx = imx_v124_project_instance
    switch_mech = imx.initial_situation.find('3d1c6832-ae71-4465-b32f-e79260450002')
    assert len(switch_mech.imx_extensions) == 2, "Should have x extensions"
    assert len(switch_mech.extension_properties) == 8, "Should have x extensions props"


@pytest.mark.slow
def test_imx_parse_project_v500(imx_v500_project_instance):
    imx = imx_v500_project_instance
    assert imx.file.imx_version == "5.0.0", "imx version should be 5.0.0"
    assert len(list(imx.initial_situation.get_all())) == 3689, "objects in tree should is off"
    assert len(imx.initial_situation.get_build_exceptions()) == 0, "should not have no exceptions"
    assert imx.new_situation is None, "does not have a new situation"


@pytest.mark.slow
def test_imx_parse_v1200_zip(imx_v1200_zip_instance):
    imx = imx_v1200_zip_instance
    assert (
        imx.files.signaling_design.imx_version == "12.0.0"
    ), "imx version should be 12.0.0"
    assert len(list(imx.get_all())) == 302, "objects in tree should is off"
    assert len(imx.get_build_exceptions()) == 6, "should have x exceptions"


@pytest.mark.slow
def test_imx_parse_v1200_dir(imx_v1200_dir_instance):
    imx = imx_v1200_dir_instance
    assert (imx.files.signaling_design.imx_version == "12.0.0"), "imx version should be 12.0.0"
    assert len(list(imx.get_all())) == 302, "objects in tree should is off"
    # dir has one more extension course of mismatch on file hash for observations
    assert len(imx.get_build_exceptions()) == 7, "should have x exceptions"

