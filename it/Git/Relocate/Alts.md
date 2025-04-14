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

- Main: 
    - token-based Pull: directly from repo (`r`) to mirror (`m`)  
	  `pull from r to m`
- Secondary: edge mirror (`em`) + some deep mirror (`dm`)
	- Action based push:  
	  `-                , push from r to em , pull from em to dm`
	- PC-based hybrid:  
	  `pull from r to pc, push from pc to em, pull from em to dm`
