def test_api_get(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status == 200
    json_data = response.json() 
    print(json_data)    
    assert json_data["id"] == 1
    assert json_data["userId"] == 1
    assert json_data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    print("API GET request successful and data validated.")
    request.dispose()
    print("Test completed successfully.")