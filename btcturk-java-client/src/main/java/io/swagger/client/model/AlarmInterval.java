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
 * Gets or Sets AlarmInterval
 */
@JsonAdapter(AlarmInterval.Adapter.class)
public enum AlarmInterval {
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null),
  NUMBER_null(null);

  private Integer value;

  AlarmInterval(Integer value) {
    this.value = value;
  }

  public Integer getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static AlarmInterval fromValue(Integer input) {
    for (AlarmInterval b : AlarmInterval.values()) {
      if (b.value.equals(input)) {
        return b;
      }
    }
    return null;
  }

  public static class Adapter extends TypeAdapter<AlarmInterval> {
    @Override
    public void write(final JsonWriter jsonWriter, final AlarmInterval enumeration) throws IOException {
      jsonWriter.value(String.valueOf(enumeration.getValue()));
    }

    @Override
    public AlarmInterval read(final JsonReader jsonReader) throws IOException {
      Object value = jsonReader.nextInt();
      return AlarmInterval.fromValue((Integer)(value));
    }
  }
}