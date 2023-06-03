
AnyStr = TypeVar('AnyStr', bytes, str)


def int2ip(ipint: int) -> str:
    """Converts the integer representation of an IP address to its
    classical decimal, dot-separated (for IPv4) or hexadecimal,
    colon-separated (for IPv6) string representation.

    """
    try:
        return socket.inet_ntoa(struct.pack("!I", ipint))
    except struct.error:
        return socket.inet_ntop(
            socket.AF_INET6,
            struct.pack("!QQ", ipint >> 64, ipint & 0xFFFFFFFFFFFFFFFF),
        )


def ip2int(ipstr: AnyStr) -> int:
    """Converts the classical decimal, dot-separated, string
    representation of an IPv4 address, or the hexadecimal,
    colon-separated, string representation of an IPv6 address, to an
    integer.

    """
    if isinstance(ipstr, bytes):
        data = ipstr.decode()
    else:
        data = ipstr
    try:
        return cast(int, struct.unpack("!I", socket.inet_aton(data))[0])
    except socket.error:
        val1: int
        val2: int
        val1, val2 = struct.unpack(
            "!QQ",
            socket.inet_pton(socket.AF_INET6, data),
        )
        return (val1 << 64) + val2


ip2int("220.186.156.0")
