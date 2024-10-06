import json
import requests
import settings


class Pets:
    """API library to the site http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Request to Swagger to get valid token using email and password"""
        data = {"email": settings.VALID_EMAIL,
                "password": settings.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    def get_list_users(self) -> json:
        """Request to Swagger to get valid list of users"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        my_id = res.text
        return status, amount, my_id

    def post_pet(self) -> json:
        """Request to Swagger to create a new pet"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Rubik', "type": 'dog', "age": 3, "owner_id": my_id}

        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def get_pet_id(self) -> json:
        """Request to Swagger to get data about a pet using pet's id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        pet_data = res.json()
        status = res.status_code
        return pet_data, status

    def post_pet_photo(self):
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        file_path = 'C:/Users/shulg/PycharmProjects/Python_API_PetProject/tests/photo/dog.jpg'
        file = open(file_path, 'rb')
        doc_picture_binary = {'pic': ('image.jpg', file, 'image/jpeg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=doc_picture_binary)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def edit_pet(self) -> json:
        """Request to Swagger to change a part of data about a pet"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_new_data = {"id": pet_id,
                        "name": 'Kira', "type": 'cat', "age": 3, "owner_id": my_id}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(pet_new_data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return status, pet_id

    def put_pet_like(self) -> json:
        """Request to Swagger to put a like to a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status, pet_id

    def put_pet_comment(self) -> json:
        """Request to Swagger to put a message to a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"message": 'My super-puper-cool dog'}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        message = res.json()
        return status, message

    def delete_pet(self):
        """Request to the Swagger to delete a pet"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status
