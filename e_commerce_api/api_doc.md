# APIs
list goods
* request method: GET
* endpoints: `/goods`
* authentication: required

launch good
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
* endpoints: `/<good_id>/discontinue`
* authentication: required

update reserve
* request method: POST
* endpoints: `/somewhere`
* authentication: required

add to cart
* request method: POST
* endpoints: `/somewhere`
* authentication: required

remove from cart
* request method: POST
* endpoints: `/somewhere`
* authentication: required

purchase
* request method: POST
* endpoints: `/somewhere`
* authentication: required

generate receipt
* request method: POST
* endpoints: `/somewhere`
* authentication: required