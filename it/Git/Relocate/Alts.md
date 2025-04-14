# Alternatives

## 1st round

| Alternative        | Reliable | Secure   | Simple    | Future proof | Comment                      |
|--------------------|----------|----------| ----------|--------------|------------------------------|
|Push                | Yes      | Yes      | Yes       | Not          | Depends on GitHub actions    |
|password-based Pull | Yes      | Not      | Yes       | Yes          | Share passwords with mirrors |
|PC-based Mirror     | Not      | Yes      | Not       | Yes          | Multiple machine roles       |

## 2nd round

| Alternative        | Reliable | Secure   | Simple    | Future proof | Comment                      |
|--------------------|----------|----------| ----------|--------------|------------------------------|
|ssh-key-based Pull  | Yes      | Not      | Yes       | Yes          | Read write access            |
|token-based Pull    | Yes      | Yes      | Medium    | Medium       | New tech, Manual refresh     |

## Prototype

- Main: Token-based Pull
- Secondary: one main mirror + some slave mirror
	- PC-based hybrid:  
	  `pull from m, push to mm, pull from mm to sm`
	- Action based push:  
	  `-          , push to mm, pull from mm to sm`
