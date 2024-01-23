---
title: FastAPI v0.1.0
language_tabs:
  - shell: Shell
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="fastapi">FastAPI v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="fastapi-default">Default</h1>

## login_v1_db_login_post

<a id="opIdlogin_v1_db_login_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /v1/db_login \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /v1/db_login`

*Login*

> Body parameter

```json
{}
```

<h3 id="login_v1_db_login_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="login_v1_db_login_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="login_v1_db_login_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## list_schema_info_v1_list_tables_get

<a id="opIdlist_schema_info_v1_list_tables_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v1/list_tables \
  -H 'Accept: application/json' \
  -H 'token: string'

```

`GET /v1/list_tables`

*List Schema Info*

_summary_
Get all info about schema
Args:
    token (Annotated[str  |  None, Header, optional): _description_. Defaults to None.

Returns:
    _type_: _description_

<h3 id="list_schema_info_v1_list_tables_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|token|header|string|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="list_schema_info_v1_list_tables_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="list_schema_info_v1_list_tables_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## search_table_v1_search_tables_get

<a id="opIdsearch_table_v1_search_tables_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /v1/search_tables?table_name=string \
  -H 'Accept: application/json' \
  -H 'token: string'

```

`GET /v1/search_tables`

*Search Table*

search a table by its name

Args:
    table_name (str): _description_
    token (Annotated[str  |  None, Header, optional): _description_. Defaults to None.

Returns:
    _type_: _description_

<h3 id="search_table_v1_search_tables_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|table_name|query|string|true|none|
|token|header|string|false|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="search_table_v1_search_tables_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="search_table_v1_search_tables_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

