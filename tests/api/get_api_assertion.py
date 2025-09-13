def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer your_token_here",
            "x-api-key": "reqres-free-v1"
        }, 
    )

    # First API: List users
    response = request.get("https://reqres.in/api/users?page=2")
    assert response.status == 200
    json_data = response.json()
    print(json_data)

    # Validate first user in the "data" list
    first_user = json_data["data"][0]
    assert "id" in first_user
    assert first_user["id"] == 7
    assert first_user["email"] == "michael.lawson@reqres.in"

    # Second API: Single post
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    post_data = response.json()
    print(post_data)

    assert post_data["id"] == 1
    assert post_data["userId"] == 1
    assert post_data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"

    print("API GET requests successful and data validated.")
    request.dispose()
    print("Test completed successfully.")
