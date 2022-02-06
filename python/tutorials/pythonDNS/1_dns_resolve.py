import dns.resolver

result = dns.resolver.resolve('yiibai.com', 'A')
for ipval in result:
    print('IP: ', ipval.to_text())

cname = dns.resolver.resolve('mail.google.com', 'CNAME')
for cnameval in cname:
    print('CNAME target address: ', cnameval.target)
