from api import Pets
import allure

pt = Pets()


@allure.feature('Getting valid token')
@allure.story('Input valid email and password')
@allure.severity('blocker')
def test_get_token():
    with allure.step('Send request to get token'):
        '''Retrieve the token, status, and my_id'''
        token, status, my_id = pt.get_token()

    with allure.step('Validate token is received'):
        assert token, 'Token should not be empty'
        allure.attach(token, name='Received Token', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Validate response status is 200'):
        assert status == 200, f'Expected status 200, but got {status}'
        allure.attach(str(status), name='Response Status', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Validate my_id is present'):
        assert my_id, 'my_id should not be empty'
        allure.attach(str(my_id), name='my_id', attachment_type=allure.attachment_type.TEXT)


@allure.feature('Getting list of users')
@allure.story('Retrieve a list of users')
@allure.severity('critical')
def test_get_list_users():
    with allure.step('Send request to get the list of users'):
        '''Retrieve the status and amount of users'''
        response = pt.get_list_users()
        status = response[0]
        amount = response[1]

    with allure.step('Validate the status code is 200'):
        assert status == 200, f'Expected status 200, but got {status}'
        allure.attach(str(status), name='Response Status', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Validate the list of users is not empty'):
        assert amount, 'Amount of users should not be empty'
        allure.attach(str(amount), name='Number of Users', attachment_type=allure.attachment_type.TEXT)


@allure.feature('Post Pet')
@allure.story('Add a new pet')
@allure.severity('critical')
def test_post_pet():
    with allure.step('Send request to add a new pet'):
        '''Retrieve the pet_id and status after posting a new pet'''
        pet_id, status = pt.post_pet()

    with allure.step('Validate the status code is 200'):
        assert status == 200, f'Expected status 200, but got {status}'
        allure.attach(str(status), name='Response Status', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Validate the pet ID is received'):
        assert pet_id, 'Pet ID should not be empty'
        allure.attach(str(pet_id), name='Pet ID', attachment_type=allure.attachment_type.TEXT)


@allure.feature('Get Pet by ID')
@allure.story('Retrieve pet information by ID')
@allure.severity('critical')
def test_get_pet_id():
    with allure.step('Send request to get pet by ID'):
        '''Retrieve the pet data and status'''
        pet_data, status = pt.get_pet_id()

    with allure.step('Validate the status code is 200'):
        assert status == 200, f'Expected status 200, but got {status}'
        allure.attach(str(status), name='Response Status', attachment_type=allure.attachment_type.TEXT)

    with allure.step('Validate the pet data is received'):
        assert pet_data, 'Pet data should not be empty'
        allure.attach(str(pet_data), name='Pet Data', attachment_type=allure.attachment_type.JSON)


def test_post_pet_photo():
    status = pt.post_pet_photo()[0]
    link = pt.post_pet_photo()[1]
    assert status == 200
    assert link


def test_patch_pet():
    status = pt.edit_pet()[0]
    pet_new_data = pt.edit_pet()[1]
    assert status == 200
    assert pet_new_data


def test_put_pet_like():
    pet = pt.put_pet_like()
    status = pet[0]
    like = pet[1]
    assert status == 200
    assert like


def test_put_pet_comment():
    pet = pt.put_pet_comment()
    status = pet[0]
    message = pet[1]
    assert status == 200
    assert message


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200
