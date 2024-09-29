from api import Pets

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    token = pt.get_token()[0]
    my_id = pt.get_token()[2]
    assert token
    assert status == 200
    assert my_id


def test_list_users():
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


def test_post_pet():
    status = pt.post_pet()[0]
    pet_id = pt.post_pet()[1]
    assert status == 200
    assert pet_id


def test_get_pet_id():
    status = pt.get_pet_id()[0]
    pet_data = pt.get_pet_id()[1]
    assert status == 200
    assert pet_data


def test_post_pet_photo():
    status = pt.post_pet_photo()[0]
    link = pt.post_pet_photo()[1]
    assert status == 200
    assert link


def test_patch_pet():
    status = pt.patch_pet()[0]
    pet_new_data = pt.patch_pet()[1]
    assert status == 200
    assert pet_new_data


def test_put_pet_like():
    status = pt.put_pet_like()[0]
    like = pt.put_pet_like()[1]
    assert status == 200
    assert like


def test_put_pet_comment():
    status = pt.put_pet_comment()[0]
    comment = pt.put_pet_comment()[1]
    assert status == 200
    assert comment
