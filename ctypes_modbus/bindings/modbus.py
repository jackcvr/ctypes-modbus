# script is auto-generated

"""Usage example:
import ctypes as C

from . import bind, bind_all

lib = ...


class CType:
    modbus_t_p = C.c_void_p
    modbus_error_recovery_mode = ...
    uint32_t_p = C.c_void_p
    uint8_t_p = C.c_void_p
    uint16_t_p = C.c_void_p
    modbus_mapping_t_p = C.c_void_p


bind_all(lib, CType)


"""

import ctypes as C


def bind(restype, func, *argtypes):
    func.restype = restype
    func.argtypes = argtypes


def bind_all(lib, ctx):
    # int modbus_set_slave(modbus_t *ctx, int slave);
    bind(C.c_int, lib.modbus_set_slave, ctx.modbus_t_p, C.c_int)
    # int modbus_get_slave(modbus_t *ctx);
    bind(C.c_int, lib.modbus_get_slave, ctx.modbus_t_p)
    # int modbus_set_error_recovery(modbus_t *ctx, modbus_error_recovery_mode error_recovery);
    bind(
        C.c_int,
        lib.modbus_set_error_recovery,
        ctx.modbus_t_p,
        ctx.modbus_error_recovery_mode,
    )
    # int modbus_set_socket(modbus_t *ctx, int s);
    bind(C.c_int, lib.modbus_set_socket, ctx.modbus_t_p, C.c_int)
    # int modbus_get_socket(modbus_t *ctx);
    bind(C.c_int, lib.modbus_get_socket, ctx.modbus_t_p)
    # int modbus_get_response_timeout(modbus_t *ctx, uint32_t *to_sec, uint32_t *to_usec);
    bind(
        C.c_int,
        lib.modbus_get_response_timeout,
        ctx.modbus_t_p,
        ctx.uint32_t_p,
        ctx.uint32_t_p,
    )
    # int modbus_set_response_timeout(modbus_t *ctx, uint32_t to_sec, uint32_t to_usec);
    bind(
        C.c_int, lib.modbus_set_response_timeout, ctx.modbus_t_p, C.c_uint32, C.c_uint32
    )
    # int modbus_get_byte_timeout(modbus_t *ctx, uint32_t *to_sec, uint32_t *to_usec);
    bind(
        C.c_int,
        lib.modbus_get_byte_timeout,
        ctx.modbus_t_p,
        ctx.uint32_t_p,
        ctx.uint32_t_p,
    )
    # int modbus_set_byte_timeout(modbus_t *ctx, uint32_t to_sec, uint32_t to_usec);
    bind(C.c_int, lib.modbus_set_byte_timeout, ctx.modbus_t_p, C.c_uint32, C.c_uint32)
    # int modbus_get_indication_timeout(modbus_t *ctx, uint32_t *to_sec, uint32_t *to_usec);
    bind(
        C.c_int,
        lib.modbus_get_indication_timeout,
        ctx.modbus_t_p,
        ctx.uint32_t_p,
        ctx.uint32_t_p,
    )
    # int modbus_set_indication_timeout(modbus_t *ctx, uint32_t to_sec, uint32_t to_usec);
    bind(
        C.c_int,
        lib.modbus_set_indication_timeout,
        ctx.modbus_t_p,
        C.c_uint32,
        C.c_uint32,
    )
    # int modbus_get_header_length(modbus_t *ctx);
    bind(C.c_int, lib.modbus_get_header_length, ctx.modbus_t_p)
    # int modbus_connect(modbus_t *ctx);
    bind(C.c_int, lib.modbus_connect, ctx.modbus_t_p)
    # void modbus_close(modbus_t *ctx);
    bind(None, lib.modbus_close, ctx.modbus_t_p)
    # void modbus_free(modbus_t *ctx);
    bind(None, lib.modbus_free, ctx.modbus_t_p)
    # int modbus_flush(modbus_t *ctx);
    bind(C.c_int, lib.modbus_flush, ctx.modbus_t_p)
    # int modbus_set_debug(modbus_t *ctx, int flag);
    bind(C.c_int, lib.modbus_set_debug, ctx.modbus_t_p, C.c_int)
    # const char *modbus_strerror(int errnum);
    bind(C.c_char_p, lib.modbus_strerror, C.c_int)
    # int modbus_read_bits(modbus_t *ctx, int addr, int nb, uint8_t *dest);
    bind(C.c_int, lib.modbus_read_bits, ctx.modbus_t_p, C.c_int, C.c_int, ctx.uint8_t_p)
    # int modbus_read_input_bits(modbus_t *ctx, int addr, int nb, uint8_t *dest);
    bind(
        C.c_int,
        lib.modbus_read_input_bits,
        ctx.modbus_t_p,
        C.c_int,
        C.c_int,
        ctx.uint8_t_p,
    )
    # int modbus_read_registers(modbus_t *ctx, int addr, int nb, uint16_t *dest);
    bind(
        C.c_int,
        lib.modbus_read_registers,
        ctx.modbus_t_p,
        C.c_int,
        C.c_int,
        ctx.uint16_t_p,
    )
    # int modbus_read_input_registers(modbus_t *ctx, int addr, int nb, uint16_t *dest);
    bind(
        C.c_int,
        lib.modbus_read_input_registers,
        ctx.modbus_t_p,
        C.c_int,
        C.c_int,
        ctx.uint16_t_p,
    )
    # int modbus_write_bit(modbus_t *ctx, int coil_addr, int status);
    bind(C.c_int, lib.modbus_write_bit, ctx.modbus_t_p, C.c_int, C.c_int)
    # int modbus_write_register(modbus_t *ctx, int reg_addr, const uint16_t value);
    bind(C.c_int, lib.modbus_write_register, ctx.modbus_t_p, C.c_int, C.c_uint16)
    # int modbus_write_bits(modbus_t *ctx, int addr, int nb, const uint8_t *data);
    bind(
        C.c_int, lib.modbus_write_bits, ctx.modbus_t_p, C.c_int, C.c_int, ctx.uint8_t_p
    )
    # int modbus_write_registers(modbus_t *ctx, int addr, int nb, const uint16_t *data);
    bind(
        C.c_int,
        lib.modbus_write_registers,
        ctx.modbus_t_p,
        C.c_int,
        C.c_int,
        ctx.uint16_t_p,
    )
    # int modbus_mask_write_register(modbus_t *ctx, int addr, uint16_t and_mask, uint16_t or_mask);
    bind(
        C.c_int,
        lib.modbus_mask_write_register,
        ctx.modbus_t_p,
        C.c_int,
        C.c_uint16,
        C.c_uint16,
    )
    # int modbus_write_and_read_registers(modbus_t *ctx, int write_addr, int write_nb, const uint16_t *src, int read_addr, int read_nb, uint16_t *dest);
    bind(
        C.c_int,
        lib.modbus_write_and_read_registers,
        ctx.modbus_t_p,
        C.c_int,
        C.c_int,
        ctx.uint16_t_p,
        C.c_int,
        C.c_int,
        ctx.uint16_t_p,
    )
    # int modbus_report_slave_id(modbus_t *ctx, int max_dest, uint8_t *dest);
    bind(C.c_int, lib.modbus_report_slave_id, ctx.modbus_t_p, C.c_int, ctx.uint8_t_p)
    # modbus_mapping_t * modbus_mapping_new_start_address(unsigned int start_bits, unsigned int nb_bits, unsigned int start_input_bits, unsigned int nb_input_bits, unsigned int start_registers, unsigned int nb_registers, unsigned int start_input_registers, unsigned int nb_input_registers);
    bind(
        ctx.modbus_mapping_t_p,
        lib.modbus_mapping_new_start_address,
        C.c_uint,
        C.c_uint,
        C.c_uint,
        C.c_uint,
        C.c_uint,
        C.c_uint,
        C.c_uint,
        C.c_uint,
    )
    # modbus_mapping_t *modbus_mapping_new(int nb_bits, int nb_input_bits, int nb_registers, int nb_input_registers);
    bind(
        ctx.modbus_mapping_t_p,
        lib.modbus_mapping_new,
        C.c_int,
        C.c_int,
        C.c_int,
        C.c_int,
    )
    # void modbus_mapping_free(modbus_mapping_t *mb_mapping);
    bind(None, lib.modbus_mapping_free, ctx.modbus_mapping_t_p)
    # int modbus_send_raw_request(modbus_t *ctx, const uint8_t *raw_req, int raw_req_length);
    bind(C.c_int, lib.modbus_send_raw_request, ctx.modbus_t_p, ctx.uint8_t_p, C.c_int)
    # int modbus_send_raw_request_tid(modbus_t *ctx, const uint8_t *raw_req, int raw_req_length, int tid);
    bind(
        C.c_int,
        lib.modbus_send_raw_request_tid,
        ctx.modbus_t_p,
        ctx.uint8_t_p,
        C.c_int,
        C.c_int,
    )
    # int modbus_receive(modbus_t *ctx, uint8_t *req);
    bind(C.c_int, lib.modbus_receive, ctx.modbus_t_p, ctx.uint8_t_p)
    # int modbus_receive_confirmation(modbus_t *ctx, uint8_t *rsp);
    bind(C.c_int, lib.modbus_receive_confirmation, ctx.modbus_t_p, ctx.uint8_t_p)
    # int modbus_reply(modbus_t *ctx, const uint8_t *req, int req_length, modbus_mapping_t *mb_mapping);
    bind(
        C.c_int,
        lib.modbus_reply,
        ctx.modbus_t_p,
        ctx.uint8_t_p,
        C.c_int,
        ctx.modbus_mapping_t_p,
    )
    # int modbus_reply_exception(modbus_t *ctx, const uint8_t *req, unsigned int exception_code);
    bind(C.c_int, lib.modbus_reply_exception, ctx.modbus_t_p, ctx.uint8_t_p, C.c_uint)
    # int modbus_enable_quirks(modbus_t *ctx, unsigned int quirks_mask);
    bind(C.c_int, lib.modbus_enable_quirks, ctx.modbus_t_p, C.c_uint)
    # int modbus_disable_quirks(modbus_t *ctx, unsigned int quirks_mask);
    bind(C.c_int, lib.modbus_disable_quirks, ctx.modbus_t_p, C.c_uint)
    # void modbus_set_bits_from_byte(uint8_t *dest, int idx, const uint8_t value);
    bind(None, lib.modbus_set_bits_from_byte, ctx.uint8_t_p, C.c_int, C.c_uint8)
    # void modbus_set_bits_from_bytes(uint8_t *dest, int idx, unsigned int nb_bits, const uint8_t *tab_byte);
    bind(
        None,
        lib.modbus_set_bits_from_bytes,
        ctx.uint8_t_p,
        C.c_int,
        C.c_uint,
        ctx.uint8_t_p,
    )
    # uint8_t modbus_get_byte_from_bits(const uint8_t *src, int idx, unsigned int nb_bits);
    bind(C.c_uint8, lib.modbus_get_byte_from_bits, ctx.uint8_t_p, C.c_int, C.c_uint)
    # float modbus_get_float(const uint16_t *src);
    bind(C.c_float, lib.modbus_get_float, ctx.uint16_t_p)
    # float modbus_get_float_abcd(const uint16_t *src);
    bind(C.c_float, lib.modbus_get_float_abcd, ctx.uint16_t_p)
    # float modbus_get_float_dcba(const uint16_t *src);
    bind(C.c_float, lib.modbus_get_float_dcba, ctx.uint16_t_p)
    # float modbus_get_float_badc(const uint16_t *src);
    bind(C.c_float, lib.modbus_get_float_badc, ctx.uint16_t_p)
    # float modbus_get_float_cdab(const uint16_t *src);
    bind(C.c_float, lib.modbus_get_float_cdab, ctx.uint16_t_p)
    # void modbus_set_float(float f, uint16_t *dest);
    bind(None, lib.modbus_set_float, C.c_float, ctx.uint16_t_p)
    # void modbus_set_float_abcd(float f, uint16_t *dest);
    bind(None, lib.modbus_set_float_abcd, C.c_float, ctx.uint16_t_p)
    # void modbus_set_float_dcba(float f, uint16_t *dest);
    bind(None, lib.modbus_set_float_dcba, C.c_float, ctx.uint16_t_p)
    # void modbus_set_float_badc(float f, uint16_t *dest);
    bind(None, lib.modbus_set_float_badc, C.c_float, ctx.uint16_t_p)
    # void modbus_set_float_cdab(float f, uint16_t *dest);
    bind(None, lib.modbus_set_float_cdab, C.c_float, ctx.uint16_t_p)
