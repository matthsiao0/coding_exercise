# APIs
List goods
* request method: GET
* endpoints: `/goods`

Launch good
* request method: POST
* endpoints: `/launch`
* authentication: required

| name      | location   | type   | description           |
| ------    | ---------- | ------ | -------------         |
| goodsName | json       | str    | name of good(s)       |
| price     | json       | int    | price for one good    |
| reserve   | json       | int    |                       |
| promotion | json       | str    | message for promotion |

```
200 OK
{
    {"id": "<good_id>"}
}
```

discontinue good
* request method: DELETE
* endpoints: `/discontinue`
* authentication: required

update goods reserve
* request method: PUT
* endpoints: `/<good_id>/update`
* authentication: required

add good to cart
* request method: PUT
* endpoints: `/<user_id>/cart`
* authentication: required

remove good from cart
* request method: DELETE
* endpoints: `/<user_id>/cart/<good_id>`
* authentication: required

List shopping cart
* request method: GET
* endpoints: `/<user_id>/cart`

checkout
* request method: POST
* endpoints: `/<user_id>/cart/checkout`
* authentication: required

list orders
* request method: GET
* endpoints: `/<user_id>/orders`
* authentication: required