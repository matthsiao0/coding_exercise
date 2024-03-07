# APIs
List products
* request method: GET
* endpoints: `/products`

Launch product
* request method: POST
* endpoints: `/product`
* authentication: required

| name      | location   | type   | description           |
| ------    | ---------- | ------ | -------------         |
| productName | json       | str    | name of product(s)       |
| price     | json       | int    | price for one product    |
| reserve   | json       | int    |                       |
| promotion | json       | str    | message for promotion |

```
200 OK
{
    {"id": "<product_id>"}
}
```

discontinue product
* request method: DELETE
* endpoints: `/product/<product_id>`
* authentication: required

update product reserve
* request method: PUT
* endpoints: `/product/<product_id>`
* authentication: required

get product picture
* request method: GET
* endpoints: `/product/<product_id>/picture`
* authentication: required

add product to cart
* request method: POST
* endpoints: `/<user_id>/cart`
* authentication: required

remove product from cart
* request method: DELETE
* endpoints: `/<user_id>/cart/<good_id>`
* authentication: required

List shopping cart
* request method: GET
* endpoints: `/<user_id>/cart`

checkout
* request method: POST
* endpoints: `/<user_id>/cart`
* authentication: required

list orders
* request method: GET
* endpoints: `/<user_id>/orders`
* authentication: required