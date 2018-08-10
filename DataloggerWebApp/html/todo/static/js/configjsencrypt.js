var PUBLIC_RSA_KEY = "-----BEGIN PUBLIC KEY-----\
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCXcvanpwztVH1jW+nuATYaE4w3\
meCvLvyX2F4llPgm/lfVywRh+Na9wI6tPNIDGW5wRx7zw+S2ROmmXw7VTWq1E1Zn\
8c7a4GKhFqSz+boxTurPxjb6lf/kTBBcr1NgG4uuf/N2GWVxHOp7ZwBfRanRHY9p\
zlUevoaRVh63iJZaTQIDAQAB\
-----END PUBLIC KEY-----\
";

var PRIVATE_RCS_KEY = "-----BEGIN RSA PRIVATE KEY-----\
MIICWwIBAAKBgQCXcvanpwztVH1jW+nuATYaE4w3meCvLvyX2F4llPgm/lfVywRh\
+Na9wI6tPNIDGW5wRx7zw+S2ROmmXw7VTWq1E1Zn8c7a4GKhFqSz+boxTurPxjb6\
lf/kTBBcr1NgG4uuf/N2GWVxHOp7ZwBfRanRHY9pzlUevoaRVh63iJZaTQIDAQAB\
AoGAJhhX7OH7QXOAOs7y79hEKJkEKzQ8rTQve26EeAWZyg0uQOvZRV+XfJGEEhV7\
aiYqfnmVUpHS5Po+n4fHrmXT0idWPFi+g22DxdGmgJzOYUa2c3N3qkvp0IaPHYRH\
oZTPiwD6l9imx8qnul5AUCf8cH75nsvt0g5Xk+4be3SXZ4ECQQC+SHkb26oIapsI\
0x1+fWQtesk8+6rG3vugsMczn63WsAHPvrZZ/sx5CFeb/mAdkcplosbRXVZIRXiQ\
ahF9QrOtAkEAy8ENbcAwpCz1LsBUqd88dWCmJav2+QJfGvjnOSAro428bUf6GlSj\
SEid+kSwR2BGxS8+yOd6QQaQDrfG20AVIQJAD+kvd0ze4uVHIW3FwZXqkoL54MeK\
eCadE8q0XXS0rIb7H8vqo4vSvSwdZ0XV86MFMYpy5X7QgCqO8kRsQfUZ4QJAFP+G\
RMNDwAeqFPFZSFBrSKV3Ofao8yydZIg2PBrmpGpc+t4qFkCWu0JQlZQynoh7gqLF\
06qXXNAyVHH4GmxWQQJAQqMaY7+F1O/5FOX26wr9XHhuNvBKUBjujc9CLLnB/89p\
qdON9SnYgeK7d2BAadOXKt2Blglm4GHEF5aYW8ayzg==\
-----END RSA PRIVATE KEY-----\
";

var encSvc = new JSEncrypt();
encSvc.setPublicKey(PUBLIC_RSA_KEY);
// encSvc.setPrivateKey(PRIVATE_RCS_KEY);
// var s1 = encSvc.encrypt('secreto to encrypt')
// console.log("s1",s1)
// var s2 = encSvc.encrypt('admin')
// console.log("s2",s2)
// var d2 = encSvc.decrypt(s2)
// console.log("s2",d2)
