/* 
 * BtcTurk API 3.0
 *
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// CardRegistrationRequestViewModel
    /// </summary>
    [DataContract]
        public partial class CardRegistrationRequestViewModel :  IEquatable<CardRegistrationRequestViewModel>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CardRegistrationRequestViewModel" /> class.
        /// </summary>
        /// <param name="addressName">addressName (required).</param>
        /// <param name="address">address (required).</param>
        /// <param name="cityId">cityId (required).</param>
        /// <param name="districtId">districtId (required).</param>
        public CardRegistrationRequestViewModel(string addressName = default(string), string address = default(string), long? cityId = default(long?), long? districtId = default(long?))
        {
            // to ensure "addressName" is required (not null)
            if (addressName == null)
            {
                throw new InvalidDataException("addressName is a required property for CardRegistrationRequestViewModel and cannot be null");
            }
            else
            {
                this.AddressName = addressName;
            }
            // to ensure "address" is required (not null)
            if (address == null)
            {
                throw new InvalidDataException("address is a required property for CardRegistrationRequestViewModel and cannot be null");
            }
            else
            {
                this.Address = address;
            }
            // to ensure "cityId" is required (not null)
            if (cityId == null)
            {
                throw new InvalidDataException("cityId is a required property for CardRegistrationRequestViewModel and cannot be null");
            }
            else
            {
                this.CityId = cityId;
            }
            // to ensure "districtId" is required (not null)
            if (districtId == null)
            {
                throw new InvalidDataException("districtId is a required property for CardRegistrationRequestViewModel and cannot be null");
            }
            else
            {
                this.DistrictId = districtId;
            }
        }
        
        /// <summary>
        /// Gets or Sets AddressName
        /// </summary>
        [DataMember(Name="addressName", EmitDefaultValue=false)]
        public string AddressName { get; set; }

        /// <summary>
        /// Gets or Sets Address
        /// </summary>
        [DataMember(Name="address", EmitDefaultValue=false)]
        public string Address { get; set; }

        /// <summary>
        /// Gets or Sets CityId
        /// </summary>
        [DataMember(Name="cityId", EmitDefaultValue=false)]
        public long? CityId { get; set; }

        /// <summary>
        /// Gets or Sets DistrictId
        /// </summary>
        [DataMember(Name="districtId", EmitDefaultValue=false)]
        public long? DistrictId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class CardRegistrationRequestViewModel {\n");
            sb.Append("  AddressName: ").Append(AddressName).Append("\n");
            sb.Append("  Address: ").Append(Address).Append("\n");
            sb.Append("  CityId: ").Append(CityId).Append("\n");
            sb.Append("  DistrictId: ").Append(DistrictId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as CardRegistrationRequestViewModel);
        }

        /// <summary>
        /// Returns true if CardRegistrationRequestViewModel instances are equal
        /// </summary>
        /// <param name="input">Instance of CardRegistrationRequestViewModel to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(CardRegistrationRequestViewModel input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.AddressName == input.AddressName ||
                    (this.AddressName != null &&
                    this.AddressName.Equals(input.AddressName))
                ) && 
                (
                    this.Address == input.Address ||
                    (this.Address != null &&
                    this.Address.Equals(input.Address))
                ) && 
                (
                    this.CityId == input.CityId ||
                    (this.CityId != null &&
                    this.CityId.Equals(input.CityId))
                ) && 
                (
                    this.DistrictId == input.DistrictId ||
                    (this.DistrictId != null &&
                    this.DistrictId.Equals(input.DistrictId))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.AddressName != null)
                    hashCode = hashCode * 59 + this.AddressName.GetHashCode();
                if (this.Address != null)
                    hashCode = hashCode * 59 + this.Address.GetHashCode();
                if (this.CityId != null)
                    hashCode = hashCode * 59 + this.CityId.GetHashCode();
                if (this.DistrictId != null)
                    hashCode = hashCode * 59 + this.DistrictId.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
