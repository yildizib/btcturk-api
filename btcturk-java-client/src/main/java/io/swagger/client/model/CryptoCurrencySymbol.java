/*
 * BtcTurk API 3.0
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.annotations.SerializedName;
import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Gets or Sets CryptoCurrencySymbol
 */
@JsonAdapter(CryptoCurrencySymbol.Adapter.class)
public enum CryptoCurrencySymbol {
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null);

  private Integer value;

  CryptoCurrencySymbol(Integer value) {
    this.value = value;
  }

  public Integer getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static CryptoCurrencySymbol fromValue(Integer input) {
    for (CryptoCurrencySymbol b : CryptoCurrencySymbol.values()) {
      if (b.value.equals(input)) {
        return b;
      }
    }
    return null;
  }

  public static class Adapter extends TypeAdapter<CryptoCurrencySymbol> {
    @Override
    public void write(final JsonWriter jsonWriter, final CryptoCurrencySymbol enumeration) throws IOException {
      jsonWriter.value(String.valueOf(enumeration.getValue()));
    }

    @Override
    public CryptoCurrencySymbol read(final JsonReader jsonReader) throws IOException {
      Object value = jsonReader.nextInt();
      return CryptoCurrencySymbol.fromValue((Integer)(value));
    }
  }
}
