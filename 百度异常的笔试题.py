def getValue():
    try:
        return 1
    except Exception:
        return 2
    finally:
        return 3

print(getValue()) # 打印结果是几  13    23    12























